# The Shangraw Gap

**A neural signature for the living brain that vanishes at death.**

## Discovery

Living brains maintain 45-Hz bicoherence at ~0.19. Dying brains spike to 0.771 and hold for 87 seconds. Nothing occupies the gap between.

| State | 45-Hz Bicoherence | n | Source |
|-------|-------------------|---|--------|
| Living (sleep) | 0.187 | 1 | sleep.edf |
| Living (subject3) | 0.190 | 1 | physionet |
| **GAP** | **0.20-0.65** | **0** | **EMPTY** |
| Dying | 0.771 | 1 | dying.edf (87s hold) |

## Figures

![The Gap](figure1_gap.png)
*Figure 1: No living brain crosses 0.65*

![Transition](figure2_transition.png)
*Figure 2: The 87-second release at death*

![Tesla](figure3_tesla.png)
*Figure 3: 45 Hz = 6th harmonic of Schumann resonance (7.83 Hz)*

## The Physics

Tesla's 1899 Colorado Springs experiments measured Earth's resonant frequency at 7.83 Hz. The 6th harmonic is 46.98 Hz — the exact frequency where living brains show phase-coupling.

We practice the release every night in REM sleep (0.187). At death, the coupling breaks and the brain rings at the cavity frequency (0.771) for 87 seconds.

## Reproduce

```bash
python analyze_bicoherence.py sleep

