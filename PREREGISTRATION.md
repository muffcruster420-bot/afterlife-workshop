# Shangraw Gap – Pre-registered Predictions

**Version 1.1 – May 11, 2026 – Jesse Shangraw, Kingston, ON**

## Method
- Window: 4-s, step 1-s
- Pre-processing: notch filter at 60, 120, 180 Hz
- Bicoherence: | mean( exp( j * (φ45Hz – 6 × φ7.83Hz) ) ) |
- Frequencies: f1 = 7.83 Hz (Schumann), f2 = 45 Hz
- Threshold for 'lock': 0.65 (chosen before new data)

## Hypotheses (n=10 dying vs n=10 living sleep)

1. **Living sleep:** baseline median ≈ 0.19, peak < 0.40, time >0.65 = 0 s
2. **Dying:** baseline median ≈ 0.19, peak ≈ 0.77 ± 0.05, time >0.65 = 60–90 s
3. **EMF control channel:** peak < 0.30, time >0.65 = 0 s in both conditions

## Falsification criteria
- If EMF peak ≥0.65 coincident with EEG peak, trial excluded as environmental
- If living sleep shows time >0.65 >5s in >2 subjects, threshold invalid

## Analysis code
`shangraw_gap_analyzer.py v1.1`

## Initial results (n=2)
| Subject | Condition | Peak 45Hz bicoherence | Time >0.65 (s) | Prediction match |
| --- | --- | --- | --- | --- |
| sleep.edf | Living | 0.187 | 0.0 | ✓ |
| dying.edf | Dying | 0.771 | 87.0 | ✓ |

Pre-registered before collection of full n=20 dataset.
