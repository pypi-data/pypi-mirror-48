from __future__ import division

import logging

import nengo.utils.numpy as npext
from nengo.exceptions import BuildError
from nengo.utils.stdlib import groupby
import numpy as np

from nengo_loihi.discretize import bias_to_manexp
from nengo_loihi.nxsdk_obfuscation import d, d_get, d_func, d_set
from nengo_loihi.hardware.nxsdk_objects import (
    LoihiSpikeInput,
    MAX_COMPARTMENT_CFGS,
    MAX_VTH_CFGS,
)
from nengo_loihi.hardware.nxsdk_shim import (
    micro_gen,
    NxsdkBoard,
    SpikeGen,
    TraceConfigGenerator,
)
from nengo_loihi.inputs import SpikeInput

logger = logging.getLogger(__name__)


def build_board(board, seed=None):
    n_chips = board.n_chips
    n_cores_per_chip = board.n_cores_per_chip
    n_synapses_per_core = board.n_synapses_per_core
    nxsdk_board = NxsdkBoard(
        board.board_id, n_chips, n_cores_per_chip, n_synapses_per_core)

    # add our own attribute for storing our spike generator
    assert not hasattr(nxsdk_board, 'global_spike_generator')
    nxsdk_board.global_spike_generator = SpikeGen(nxsdk_board)

    # custom attr for storing SpikeInputs (filled in build_input)
    assert not hasattr(nxsdk_board, 'spike_inputs')
    nxsdk_board.spike_inputs = {}

    # build all chips
    assert len(board.chips) == len(d_get(nxsdk_board, b'bjJDaGlwcw=='))
    rng = np.random.RandomState(seed)
    for chip, nxsdk_chip in zip(
            board.chips, d_get(nxsdk_board, b'bjJDaGlwcw==')):
        logger.debug("Building chip %s", chip)
        seed = rng.randint(npext.maxint)
        build_chip(nxsdk_chip, chip, seed=seed)

    return nxsdk_board


def build_chip(nxsdk_chip, chip, seed=None):
    assert len(chip.cores) == len(d_get(nxsdk_chip, b'bjJDb3Jlcw=='))
    rng = np.random.RandomState(seed)
    for core, nxsdk_core in zip(
            chip.cores, d_get(nxsdk_chip, b'bjJDb3Jlcw==')):
        logger.debug("Building core %s", core)
        seed = rng.randint(npext.maxint)
        build_core(nxsdk_core, core, seed=seed)


def build_core(nxsdk_core, core, seed=None):  # noqa: C901
    assert len(core.compartment_cfgs) < MAX_COMPARTMENT_CFGS
    assert len(core.vth_cfgs) < MAX_VTH_CFGS

    logger.debug("- Configuring compartments")
    for i, cfg in enumerate(core.compartment_cfgs):
        d_func(d_get(nxsdk_core, b'Y3hQcm9maWxlQ2Zn')[i], b'Y29uZmlndXJl',
               kwargs={b'ZGVjYXlW': cfg.decay_v,
                       b'ZGVjYXlV': cfg.decay_u,
                       b'cmVmcmFjdERlbGF5': cfg.refract_delay,
                       b'ZW5hYmxlTm9pc2U=': cfg.enable_noise,
                       b'YmFwQWN0aW9u': 1,
                       })

    logger.debug("- Configuring vth_cfgs")
    for i, cfg in enumerate(core.vth_cfgs):
        d_func(d_get(nxsdk_core, b'dnRoUHJvZmlsZUNmZw==')[i],
               b'c3RhdGljQ2Zn', b'Y29uZmlndXJl',
               kwargs={b'dnRo': cfg.vth})

    logger.debug("- Configuring synapse_cfgs")
    for i, cfg in enumerate(core.synapse_cfgs):
        if cfg is None:
            continue

        obj = d_get(nxsdk_core, b'c3luYXBzZUZtdA==')[i]
        d_set(obj, b'd2d0TGltaXRNYW50', val=cfg.weight_limit_mant)
        d_set(obj, b'd2d0TGltaXRFeHA=', val=cfg.weight_limit_exp)
        d_set(obj, b'd2d0RXhw', val=cfg.weight_exp)
        d_set(obj, b'ZGlzY01heFdndA==', val=cfg.disc_max_weight)
        d_set(obj, b'bGVhcm5pbmdDZmc=', val=cfg.learning_cfg)
        d_set(obj, b'dGFnQml0cw==', val=cfg.tag_bits)
        d_set(obj, b'ZGx5Qml0cw==', val=cfg.delay_bits)
        d_set(obj, b'd2d0Qml0cw==', val=cfg.weight_bits)
        d_set(obj, b'cmV1c2VTeW5EYXRh', val=cfg.reuse_synapse_data)
        d_set(obj, b'bnVtU3luYXBzZXM=', val=cfg.n_synapses)
        d_set(obj, b'Y0lkeE9mZnNldA==', val=cfg.idx_offset)
        d_set(obj, b'Y0lkeE11bHQ=', val=cfg.idx_mult)
        d_set(obj, b'c2tpcEJpdHM=', val=cfg.skip_bits)
        d_set(obj, b'aWR4Qml0cw==', val=cfg.idx_bits)
        d_set(obj, b'c3luVHlwZQ==', val=cfg.synapse_type)
        d_set(obj, b'ZmFub3V0VHlwZQ==', val=cfg.fanout_type)
        d_set(obj, b'Y29tcHJlc3Npb24=', val=cfg.compression)
        d_set(obj, b'c3RkcFByb2ZpbGU=', val=cfg.stdp_cfg)
        d_set(obj, b'aWdub3JlRGx5', val=cfg.ignore_delay)

    logger.debug("- Configuring stdp_pre_cfgs")
    for i, trace_cfg in enumerate(core.stdp_pre_cfgs):
        tcg = TraceConfigGenerator()
        tc = d_func(tcg, b'Z2VuVHJhY2VDZmc=',
                    kwargs={b'dGF1': trace_cfg.tau,
                            b'c3Bpa2VMZXZlbEludA==': trace_cfg.spike_int,
                            b'c3Bpa2VMZXZlbEZyYWM=': trace_cfg.spike_frac,
                            })
        d_get(tc, b'd3JpdGVUb1JlZ2lzdGVy')(
            d_get(nxsdk_core, b'c3RkcFByZUNmZw==')[i])

    # --- seed randomness
    def seed_trace(trace_random, rng):
        trace_random.random0 = rng.randint(2**32)
        trace_random.random1 = rng.randint(2**32)
        trace_random.random2 = rng.randint(2**32)

    rng = np.random.RandomState(seed)
    # neuron noise
    # TODO: how to set neuron noise?
    # d_set (nxsdk_core, b'ZGVuZHJpdGVSYW5kb20=', b'd29yZA==',
    #        val=rng.randint(2 ** 32))
    # pre trace rounding
    seed_trace(d_get(nxsdk_core, b'c3RkcFByZVJhbmRvbQ=='), rng)
    # post trace rounding
    seed_trace(d_get(nxsdk_core, b'c3RkcFBvc3RSYW5kb20='), rng)
    # soma activity trace rounding
    seed_trace(d_get(nxsdk_core, b'c29tYVJhbmRvbQ=='), rng)
    # synaptic rounding
    d_set(nxsdk_core,
          b'c3luYXBzZVJlcGFja1JhbmRvbQ==',
          b'd29yZA==',
          val=rng.randint(2 ** 32))

    # --- learning
    first_learning_index = None
    for synapse in core.iterate_synapses():
        if synapse.learning and first_learning_index is None:
            first_learning_index = core.synapse_axons[synapse][0]
            core.learning_coreid = d_get(nxsdk_core, b'aWQ=')
            break

    num_stdp = 0
    if first_learning_index is not None:
        for synapse in core.iterate_synapses():
            assert synapse.learning, (
                "Currently, all synapses on core are learning or none are")

            axons = np.array(core.synapse_axons[synapse])
            if synapse.learning:
                num_stdp += len(axons)
                assert np.all(axons >= first_learning_index)

    if num_stdp > 0:
        logger.debug("- Configuring PES learning")
        # add configurations tailored to PES learning
        d_func(nxsdk_core, b'c3RkcENmZw==', b'Y29uZmlndXJl',
               kwargs={b'Zmlyc3RMZWFybmluZ0luZGV4': first_learning_index,
                       b'bnVtUmV3YXJkQXhvbnM=': 0,
                       })

        assert core.stdp_pre_cfg_idx is None
        assert core.stdp_cfg_idx is None
        core.stdp_pre_cfg_idx = 0  # hard-code for now
        core.stdp_cfg_idx = 0  # hard-code for now (also in synapse_cfg)
        d_func(d_get(nxsdk_core, b'c3RkcFByZVByb2ZpbGVDZmc=')[0],
               b'Y29uZmlndXJl',
               kwargs={b'dXBkYXRlQWx3YXlz': 1,
                       b'bnVtVHJhY2Vz': 0,
                       b'bnVtVHJhY2VIaXN0': 0,
                       b'c3RkcFByb2ZpbGU=': 0
                       })

        # stdp config for positive error
        d_func(d_get(nxsdk_core, b'c3RkcFByb2ZpbGVDZmc=')[0],
               b'Y29uZmlndXJl',
               kwargs={b'dUNvZGVQdHI=': 0,
                       b'ZGVjaW1hdGVFeHA=': 0,
                       b'bnVtUHJvZHVjdHM=': 1,
                       b'cmVxdWlyZVk=': 1,
                       b'dXNlc1hlcG9jaA==': 1,
                       })

        # Microcode for the learning rule. `u1` evaluates the learning rule
        # every 2**1 timesteps, `x1` is the pre-trace, `y1` is the post-trace,
        # and 2^-7 is the learning rate.
        ucode = d_get(micro_gen, b'cnVsZVRvVUNvZGU=')(
            [d(b'ZHcgPSB1MSp4MSp5MSooMl4tNyk=')],
            **{d(b'ZG9PcHRpbWl6ZQ=='): False})
        assert d_get(ucode, b'bnVtVUNvZGVz') == 1
        d_set(d_get(nxsdk_core, b'c3RkcFVjb2RlTWVt')[0],
              b'd29yZA==',
              val=d_get(ucode, b'dUNvZGVz')[0])

        # stdp config for negative error
        d_func(d_get(nxsdk_core, b'c3RkcFByb2ZpbGVDZmc=')[1],
               b'Y29uZmlndXJl',
               kwargs={b'dUNvZGVQdHI=': 1,
                       b'ZGVjaW1hdGVFeHA=': 0,
                       b'bnVtUHJvZHVjdHM=': 1,
                       b'cmVxdWlyZVk=': 1,
                       b'dXNlc1hlcG9jaA==': 1,
                       })
        # use negative version of above microcode rule
        ucode = d_get(micro_gen, b'cnVsZVRvVUNvZGU=')(
            [d(b'ZHcgPSAtdTEqeDEqeTEqKDJeLTcp')],
            **{d(b'ZG9PcHRpbWl6ZQ=='): False})
        assert d_get(ucode, b'bnVtVUNvZGVz') == 1
        d_set(d_get(nxsdk_core, b'c3RkcFVjb2RlTWVt')[1],
              b'd29yZA==',
              val=d_get(ucode, b'dUNvZGVz')[0])

        tcg = TraceConfigGenerator()
        tc = d_func(tcg, b'Z2VuVHJhY2VDZmc=',
                    kwargs={b'dGF1': 0,
                            b'c3Bpa2VMZXZlbEludA==': 0,
                            b'c3Bpa2VMZXZlbEZyYWM=': 0,
                            })
        d_get(tc, b'd3JpdGVUb1JlZ2lzdGVy')(
            d_get(nxsdk_core, b'c3RkcFBvc3RDZmc=')[0])

    # TODO: allocator should be checking that vmin, vmax are the same
    #   for all blocks on a core
    n_compartments = 0
    if len(core.blocks) > 0:
        block0 = core.blocks[0]
        vmin, vmax = block0.compartment.vmin, block0.compartment.vmax
        assert all(block.compartment.vmin == vmin
                   for block in core.blocks)
        assert all(block.compartment.vmax == vmax
                   for block in core.blocks)
        neg_limit = np.log2(-vmin + 1)
        pos_limit = (np.log2(vmax + 1) - 9) * 0.5
        assert int(neg_limit) == neg_limit
        assert int(pos_limit) == pos_limit

        noise_exp = block0.compartment.noise_exp
        noise_offset = block0.compartment.noise_offset
        noise_at_membrane = block0.compartment.noise_at_membrane
        assert all(block.compartment.noise_exp == noise_exp
                   for block in core.blocks)
        assert all(block.compartment.noise_offset == noise_offset
                   for block in core.blocks)
        assert all(block.compartment.noise_at_membrane == noise_at_membrane
                   for block in core.blocks)

        if noise_exp < d(b'Nw==', int):
            # unexpected shifting: exp less than threshold acts as exp + 1
            noise_exp = noise_exp - 1

        d_func(nxsdk_core, b'ZGVuZHJpdGVTaGFyZWRDZmc=', b'Y29uZmlndXJl',
               kwargs={b'cG9zVm1MaW1pdA==': int(pos_limit),
                       b'bmVnVm1MaW1pdA==': int(neg_limit),
                       b'bm9pc2VFeHAw': noise_exp,
                       b'bm9pc2VNYW50T2Zmc2V0MA==': noise_offset,
                       b'bm9pc2VBdERlbmRPclZt': noise_at_membrane,
                       })

        d_func(nxsdk_core, b'ZGVuZHJpdGVBY2N1bUNmZw==', b'Y29uZmlndXJl',
               kwargs={b'ZGVsYXlCaXRz': 3})

        for block, compartment_idxs, ax_range in core.iterate_blocks():
            build_block(nxsdk_core, core, block, compartment_idxs, ax_range)
            n_compartments = max(max(compartment_idxs) + 1, n_compartments)

    for inp, compartment_idxs in core.iterate_inputs():
        build_input(nxsdk_core, core, inp, compartment_idxs)

    logger.debug("- Configuring n_updates=%d", n_compartments // 4 + 1)
    d_func(nxsdk_core, b'bnVtVXBkYXRlcw==', b'Y29uZmlndXJl',
           kwargs={b'bnVtVXBkYXRlcw==': n_compartments // 4 + 1,
                   b'bnVtU3RkcA==': num_stdp,
                   })

    d_set(
        d_get(nxsdk_core, b'ZGVuZHJpdGVUaW1lU3RhdGU=')[0], b'dGVwb2No', val=2)
    d_set(d_get(nxsdk_core, b'dGltZVN0YXRl')[0], b'dGVwb2No', val=2)


def build_block(nxsdk_core, core, block, compartment_idxs, ax_range):
    assert block.compartment.scale_u is False
    assert block.compartment.scale_v is False

    logger.debug("Building %s on core.id=%d", block, nxsdk_core.id)

    for i, bias in enumerate(block.compartment.bias):
        bman, bexp = bias_to_manexp(bias)
        icx = core.compartment_cfg_idxs[block][i]
        ivth = core.vth_cfg_idxs[block][i]

        ii = compartment_idxs[i]
        d_func(d_get(nxsdk_core, b'Y3hDZmc=')[ii], b'Y29uZmlndXJl', kwargs={
            b'Ymlhcw==': bman,
            b'Ymlhc0V4cA==': bexp,
            b'dnRoUHJvZmlsZQ==': ivth,
            b'Y3hQcm9maWxl': icx,
        })

        phasex = d(b'cGhhc2UlZA==') % (ii % 4,)
        d_get(d_get(nxsdk_core, b'Y3hNZXRhU3RhdGU=')[ii // 4],
              b'Y29uZmlndXJl')(**{phasex: 2})

    logger.debug("- Building %d synapses", len(block.synapses))
    for synapse in block.synapses:
        build_synapse(nxsdk_core, core, block, synapse, compartment_idxs)

    logger.debug("- Building %d axons", len(block.axons))
    all_axons = []  # (compartment, atom, type, tchip_id, tcore_id, taxon_id)
    for axon in block.axons:
        all_axons.extend(collect_axons(nxsdk_core, core, block, axon,
                                       compartment_idxs))

    build_axons(nxsdk_core, core, block, all_axons)

    logger.debug("- Building %d probes", len(block.probes))
    for probe in block.probes:
        build_probe(nxsdk_core, core, block, probe, compartment_idxs)


def build_input(nxsdk_core, core, spike_input, compartment_idxs):
    assert len(spike_input.axons) > 0
    nxsdk_board = d_get(nxsdk_core, b'cGFyZW50', b'cGFyZW50')

    assert isinstance(spike_input, SpikeInput)
    loihi_input = LoihiSpikeInput()
    loihi_input.set_axons(core.board, nxsdk_board, spike_input)
    assert spike_input not in nxsdk_board.spike_inputs
    nxsdk_board.spike_inputs[spike_input] = loihi_input

    # add any pre-existing spikes to spikegen
    for t in spike_input.spike_times():
        spikes = spike_input.spike_idxs(t)
        for spike in loihi_input.spikes_to_loihi(t, spikes):
            assert spike.axon.atom == 0, (
                "Cannot send population spikes through spike generator")
            d_func(nxsdk_board.global_spike_generator, b'YWRkU3Bpa2U=',
                   kwargs={b'dGltZQ==': spike.time,
                           b'Y2hpcElk': spike.axon.chip_id,
                           b'Y29yZUlk': spike.axon.core_id,
                           b'YXhvbklk': spike.axon.axon_id,
                           })


def build_synapse(  # noqa C901
        nxsdk_core, core, block, synapse, compartment_idxs):
    axon_ids = core.synapse_axons[synapse]

    synapse_cfg_idx = core.synapse_cfg_idxs[synapse]
    stdp_pre_cfg_idx = core.stdp_pre_cfg_idxs[synapse]

    atom_bits = synapse.atom_bits()
    axon_bits = synapse.axon_bits()
    atom_bits_extra = synapse.atom_bits_extra()

    target_compartments = set()
    synapse_map = {}  # map weight_idx to (ptr, pop_size, len)
    total_synapse_ptr = int(core.synapse_entries[synapse][0])
    for axon_idx, axon_id in enumerate(axon_ids):
        assert axon_id <= 2**axon_bits

        weight_idx = int(synapse.axon_weight_idx(axon_idx))
        base = synapse.axon_compartment_base(axon_idx)

        if weight_idx not in synapse_map:
            weights = synapse.weights[weight_idx]
            indices = synapse.indices[weight_idx]
            weights = weights // synapse.synapse_cfg.scale
            assert weights.ndim == 2
            assert weights.shape == indices.shape
            assert np.all(weights <= 255) and np.all(weights >= -256), str(
                weights)
            n_populations, n_compartments = weights.shape

            synapse_map[weight_idx] = (
                total_synapse_ptr, n_populations, n_compartments)

            for p in range(n_populations):
                for q in range(n_compartments):
                    compartment_idx = compartment_idxs[indices[p, q]]
                    d_func(
                        d_get(nxsdk_core, b'c3luYXBzZXM=')[total_synapse_ptr],
                        b'Y29uZmlndXJl',
                        kwargs={b'Q0lkeA==': compartment_idx,
                                b'V2d0': weights[p, q],
                                b'c3luRm10SWQ=': synapse_cfg_idx,
                                b'THJuRW4=': int(synapse.learning),
                                })
                    target_compartments.add(compartment_idx)
                    total_synapse_ptr += 1

        synapse_ptr, n_populations, n_compartments = synapse_map[weight_idx]
        assert n_populations <= 2**atom_bits

        if base is None:
            # this is a dummy axon with no weights, so set n_compartments to 0
            synapse_ptr = 0
            n_compartments = 0
            base = 0
        else:
            base = int(base)

        assert base <= d(b'MjU2', int), "Currently limited by hardware"
        d_set(d_get(nxsdk_core, b'c3luYXBzZU1hcA==')[axon_id],
              b'c3luYXBzZVB0cg==', val=synapse_ptr)
        d_set(d_get(nxsdk_core, b'c3luYXBzZU1hcA==')[axon_id],
              b'c3luYXBzZUxlbg==', val=n_compartments)
        if synapse.pop_type == 0:  # discrete
            assert n_populations == 1
            d_func(d_get(nxsdk_core, b'c3luYXBzZU1hcA==')[axon_id],
                   b'ZGlzY3JldGVNYXBFbnRyeQ==', b'Y29uZmlndXJl',
                   kwargs={b'Y3hCYXNl': base})
        elif synapse.pop_type == 16:  # pop16
            d_set(d_get(nxsdk_core, b'c3luYXBzZU1hcA==')[axon_id],
                  b'cG9wU2l6ZQ==', val=n_populations)
            assert base % 4 == 0
            d_func(d_get(nxsdk_core, b'c3luYXBzZU1hcA==')[axon_id],
                   b'cG9wdWxhdGlvbjE2TWFwRW50cnk=', b'Y29uZmlndXJl',
                   kwargs={b'Y3hCYXNl': base // 4,
                           b'YXRvbUJpdHM=': atom_bits_extra,
                           })
        elif synapse.pop_type == 32:  # pop32
            d_set(d_get(nxsdk_core, b'c3luYXBzZU1hcA==')[axon_id],
                  b'cG9wU2l6ZQ==', val=n_populations)
            d_func(d_get(nxsdk_core, b'c3luYXBzZU1hcA==')[axon_id],
                   b'cG9wdWxhdGlvbjMyTWFwRW50cnk=', b'Y29uZmlndXJl',
                   kwargs={b'Y3hCYXNl': base})
        else:
            raise BuildError("Synapse: unrecognized pop_type: %s" % (
                synapse.pop_type,))

        if synapse.learning:
            assert core.stdp_pre_cfg_idx is not None
            assert stdp_pre_cfg_idx is not None
            d_func(d_get(nxsdk_core, b'c3luYXBzZU1hcA==')[axon_id + 1],
                   b'c2luZ2xlVHJhY2VFbnRyeQ==', b'Y29uZmlndXJl',
                   kwargs={b'cHJlUHJvZmlsZQ==': core.stdp_pre_cfg_idx,
                           b'dGNz': stdp_pre_cfg_idx,
                           })

    assert total_synapse_ptr == core.synapse_entries[synapse][1], (
        "Synapse pointer did not align with precomputed synapse length")

    if synapse.learning:
        assert core.stdp_cfg_idx is not None
        for compartment in target_compartments:
            # TODO: check that no compartment configured by multiple synapses
            d_func(d_get(nxsdk_core, b'c3RkcFBvc3RTdGF0ZQ==')[compartment],
                   b'Y29uZmlndXJl',
                   kwargs={b'c3RkcFByb2ZpbGU=': core.stdp_cfg_idx,
                           b'dHJhY2VQcm9maWxl': 3  # TODO: why this value
                           })


def collect_axons(nxsdk_core, core, block, axon, compartment_ids):
    synapse = axon.target
    tchip_idx, tcore_idx, tsyn_idxs = core.board.find_synapse(synapse)
    nxsdk_board = d_get(nxsdk_core, b'cGFyZW50', b'cGFyZW50')
    tchip_id = d_get(d_get(nxsdk_board, b'bjJDaGlwcw==')[tchip_idx], b'aWQ=')
    tcore_id = d_get(d_get(d_get(nxsdk_board, b'bjJDaGlwcw==')[tchip_idx],
                           b'bjJDb3Jlcw==')[tcore_idx],
                     b'aWQ=')

    compartment_idxs = np.arange(len(compartment_ids))
    spikes = axon.map_spikes(compartment_idxs)

    all_axons = []  # (compartment, atom, type, tchip_id, tcore_id, taxon_id)
    for compartment_id, spike in zip(compartment_ids, spikes):
        taxon_idx = int(spike.axon_id)
        taxon_id = int(tsyn_idxs[taxon_idx])
        atom = int(spike.atom)
        n_populations = synapse.axon_populations(taxon_idx)
        all_axons.append((compartment_id, atom, synapse.pop_type,
                          tchip_id, tcore_id, taxon_id))
        if synapse.pop_type == 0:  # discrete
            assert atom == 0
            assert n_populations == 1
        elif synapse.pop_type == 16 or synapse.pop_type == 32:
            n_blocks = len(core.blocks)
            assert (n_blocks == 0
                    or (n_blocks == 1 and block is core.blocks[0]))
            assert len(block.probes) == 0
            tchip_id_source = d_get(
                d_get(nxsdk_board, b'bjJDaGlwcw==')[core.chip.index], b'aWQ=')
            if tchip_id != tchip_id_source:
                raise BuildError("pop16 and pop32 weights are not "
                                 "supported across multiple chips "
                                 "(%d -> %d); this is likely raised due "
                                 "to convolutional weights being used "
                                 "with a multi-chip allocator" % (
                                     tchip_id_source, tchip_id))
        else:
            raise BuildError("Axon: unrecognized pop_type: %s" % (
                synapse.pop_type,))

    return all_axons


def build_axons(nxsdk_core, core, block, all_axons):  # noqa C901
    if len(all_axons) == 0:
        return

    pop_type0 = all_axons[0][2]
    if pop_type0 == 0:
        for (compartment_id, atom, pop_type, tchip_id, tcore_id,
             taxon_id) in all_axons:
            assert pop_type == 0, "All axons must be discrete, or none"
            assert atom == 0
            d_func(nxsdk_core, b'Y3JlYXRlRGlzY3JldGVBeG9u',
                   kwargs={b'c3JjQ3hJZA==': compartment_id,
                           b'ZHN0Q2hpcElk': tchip_id,
                           b'ZHN0Q29yZUlk': tcore_id,
                           b'ZHN0U3luTWFwSWQ=': taxon_id,
                           })

        return
    else:
        assert all(axon[2] != 0 for axon in all_axons), (
            "All axons must be discrete, or none")

    axons_by_compartment = groupby(all_axons, key=lambda x: x[0])

    axon_id = 0
    axon_map = {}
    for compartment_id, axons in axons_by_compartment:
        assert len(axons) > 0

        # axon -> (compartment, atom, type, tchip_id, tcore_id, taxon_id)
        assert all(axon[0] == compartment_id for axon in axons)
        atom = axons[0][1]
        assert all(axon[1] == atom for axon in axons), (
            "compartment atom must be the same for all axons")

        axons = sorted(axons, key=lambda a: a[2:])
        key = tuple(axon[2:] for axon in axons)
        if key not in axon_map:
            axon_id0 = axon_id
            axon_len = 0

            for axon in axons:
                pop_type, tchip_id, tcore_id, taxon_id = axon[2:]
                # note: pop_type==0 should have been handled in code above
                assert pop_type in (16, 32)
                if pop_type == 16:  # pop16
                    d_func(d_get(nxsdk_core, b'YXhvbkNmZw==')[axon_id],
                           b'cG9wMTY=', b'Y29uZmlndXJl',
                           kwargs={b'Y29yZUlk': tcore_id,
                                   b'YXhvbklk': taxon_id,
                                   })
                    axon_id += 1
                    axon_len += 1
                elif pop_type == 32:  # pop32
                    d_func(d_get(nxsdk_core, b'YXhvbkNmZw==')[axon_id],
                           b'cG9wMzJfMA==', b'Y29uZmlndXJl',
                           kwargs={b'Y29yZUlk': tcore_id,
                                   b'YXhvbklk': taxon_id,
                                   })
                    d_get(d_get(nxsdk_core, b'YXhvbkNmZw==')[axon_id + 1],
                          b'cG9wMzJfMQ==', b'Y29uZmlndXJl')()
                    axon_id += 2
                    axon_len += 2

            axon_map[key] = (axon_id0, axon_len)

        axon_ptr, axon_len = axon_map[key]
        d_func(d_get(nxsdk_core, b'YXhvbk1hcA==')[compartment_id],
               b'Y29uZmlndXJl',
               kwargs={b'cHRy': axon_ptr,
                       b'bGVu': axon_len,
                       b'YXRvbQ==': atom,
                       })


def build_probe(nxsdk_core, core, block, probe, compartment_idxs):
    key_map = {'current': 'u', 'voltage': 'v', 'spiked': 'spike'}
    assert probe.key in key_map, "probe key not found"
    key = key_map[probe.key]

    nxsdk_board = d_get(nxsdk_core, b'cGFyZW50', b'cGFyZW50')
    r = compartment_idxs[probe.slice]

    if probe.use_snip:
        probe.snip_info = dict(core_id=d_get(nxsdk_core, b'aWQ='),
                               compartment_idxs=r,
                               key=key)
    else:
        p = d_get(nxsdk_board, b'bW9uaXRvcg==', b'cHJvYmU=')(
            d_get(nxsdk_core, b'Y3hTdGF0ZQ=='), r, key)
        core.board.map_probe(probe, p)
