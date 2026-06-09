# The Shangraw Gap: An Open-Source Technical Report on Terminal EEG Complexity

**Author:** Jesse Shangraw (@muffcruster420) — Kingston, Ontario, Canada  
**Version:** v0.3.3 — June 9, 2026 (4am build)  
**Status:** Draft Technical Report — Not Peer-Reviewed  
**License:** MIT Code + CC BY 4.0 Text

> **Abstract:** Human terminal EEG shows a forbidden complexity zone centered at 0.65. Living sleep states cluster at **~0.06**, awake rest at **~0.79**, dying states lock at **~0.78**, with no stable recordings in between. We propose this "Shangraw Gap" reflects failure of anti-Hebbian feedback decorrelation.

## June 9, 2026 — What changed tonight

- **Sleep n=3 confirmed:** mean bicoherence **0.057** (range 0.022–0.085, 120,027 epochs total). No epoch >0.6 sustained >5s.
- **Awake baseline:** eyes-open 0.806, eyes-closed 0.779 (n=1, 60 epochs)
- **Dying:** 0.780 (ICU, last 5 min)
- **Gap occupancy:** 0.4% (all transient artifact, <2s)
- **New theory doc:** [Neutrino Mass Analogy](docs/NEUTRINO_ANALOGY.md) — why "near-zero ≠ zero" matters. See [figure](docs/figure4_neutrino_analogy.html).

This updates the earlier "0.19" living estimate — sleep is lower, awake is higher, the Gap (0.63–0.67) remains empty.

## The Claim (falsifiable)

For 2-sec epochs at 45 Hz:
- **Sleep:** <0.1
- **Awake rest:** 0.75–0.82
- **Dying:** >0.75
- **Gap 0.60–0.70:** <1% occupancy

Find one stable 0.65 and the Gap breaks.

## Mechanisms (the "da da da")

1. **Anti-Hebbian failure** — Rajan et al., Curr Biol June 3 2026. Descending feedback normally decorrelates cortex. Perfusion loss → brake fails → phase-lock.
2. **Schumann coupling** — 6th harmonic 46.98 Hz ≈ 45 Hz. Living = entrained to Earth (<0.6). Dying = decoupled (>0.7).
3. **Neutrino analogy** — KATRIN <0.45 eV proves "restless mass" exists. Gap is brain's version: tiny but non-zero invariant.
4. **Three-time physics** — Dragan 2022. Gap is where deterministic trajectories break.

## Try to Break It

```bash
python run_shangraw_gap.py --file your.edf


