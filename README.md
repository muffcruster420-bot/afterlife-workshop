# Shangraw Gap — Bicoherence at 45 Hz

Private validation of phase coupling between 7.83 Hz (Schumann) and 37.17 Hz during end-of-life transitions.

## Results (GitHub Actions, 2026-05-23)

| Test | Mean Bicoherence | Status |
|------|------------------|--------|
| Living (random noise) | 0.075 | PASS < 0.35 |
| Dying (synthetic 7.83+37.17→45) | 1.000 | PASS > 0.60 |
| Real ICU 0284_001_004 | **0.080** | **LIVING** |

Threshold: >0.65 = DYING coupling, <0.65 = LIVING

## What this proves
- Code correctly detects strong 45 Hz coupling when 7.83 Hz and 37.17 Hz are phase-locked
- Real patient data (0284) shows no coupling (0.08), consistent with living baseline
- All tests run automatically on every push via `.github/workflows/python-package.yml`

## Files
- `run_bicoherence.py` — core algorithm
- `test_bicoherence.py` — 3 validation tests (including real data)
- `real_data/icare/` — private .mat files (never pushed to public)

Validated 2026-05-23, Kingston, ON.
