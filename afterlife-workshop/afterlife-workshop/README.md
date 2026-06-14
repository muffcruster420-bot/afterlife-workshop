# The Shangraw Gap: An Open-Source Technical Report on Terminal EEG Complexity and Anti-Hebbian Feedback Failure
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20683811.svg)](https://doi.org/10.5281/zenodo.20683811) [![CI](https://github.com/muffcruster420-bot/afterlife-workshop/actions/workflows/ci.yml/badge.svg)](https://github.com/muffcruster420-bot/afterlife-workshop/actions) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# afterlife-workshop: The Shangraw Gap

A signal-processing framework exploring cross-frequency phase-coupling thresholds at the 6th harmonic of the Schumann Resonance (46.98 Hz, rounded to ~45 Hz) in human EEG data.

## Core Thesis
The project investigates the **Shangraw Gap**: a proposed hard physiological threshold in cross-frequency phase coupling.
1. **Living State (< 0.65):** Active biological brains suppress phase-coupling, maintaining a baseline bicoherence of ~0.19 during REM sleep ("practice release").
2. **The Shangraw Gap (0.65):** A biological insulation barrier. No sustained living EEG transcends this value.
3. **Death State (> 0.77):** Upon systemic failure, coupling spikes to ~0.771 for an ~87-second window, phase-locking with global electromagnetic cavity resonances.

## Statistical Framework
* **$H_0$ (Null Hypothesis):** The distribution of maximum 45-Hz bicoherence in living human brains (during wakefulness or REM sleep) overlaps or exceeds the 0.65 threshold ($B^2 \ge 0.65$).
* **$H_1$ (Alternative Hypothesis):** The living brain strictly regulates phase-coupling, such that $B^2 < 0.65$ universally until systemic terminal failure.

## Mathematical Definition
Bicoherence ($B^2$) measures non-linear quadratic phase coupling between three frequencies where $f_3 = f_1 + f_2$. For a signal $X(f)$:

$$B^2(f_1, f_2) = \frac{|\sum X(f_1)X(f_2)X^*(f_1+f_2)|^2}{\sum |X(f_1)X(f_2)|^2 \sum |X(f_1+f_2)|^2}$$

Where $B^2 \in [0, 1]$, where 0 is purely independent phase states and 1 is absolute phase synchronization.

## Data Sources
* **PhysioNet Sleep-EDF Database:** Public polysomnography records (e.g., `SC4001E0`, `SC4002E0`).
* **I-CARE Database:** Cardiac arrest neuroprognostication EEG data.
