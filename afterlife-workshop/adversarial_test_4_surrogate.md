# Adversarial Test 4: Random Noise / Phase Surrogate
Date: 2026-06-12
File: SC4001E0-PSG.edf (first 5 min, channel 0, 2s windows)

Results:
- REAL: mean=0.099, gap=1.01%
- SURROGATE (phase-randomized): mean=0.114, gap=1.68%

Interpretation: Destroying true phase coupling does not eliminate the Gap. Both real and surrogate data show strong depletion in 0.6-0.7 (vs 10% expected by chance). The Gap is therefore not evidence of quadratic phase coupling per se, but a robust property of the bicoherence estimator applied to sleep EEG spectra. This refutes the "cherry-picked noise" criticism while requiring the theory to be reframed around deviations from this baseline.
