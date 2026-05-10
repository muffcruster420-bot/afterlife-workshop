## Measured hold time: 87.0 seconds above 0.65 threshold
- n=1 dying.edf, 4-second windows, 1-second steps
- Peak bicoherence 0.771 at 45 Hz (7.83 + 37.17 Hz coupling)# The Afterlife Workshop
**Jesse Shangraw — Kingston, Ontario — May 9, 2026**

Every night your brain practices a 45-Hz signal locked to Earth's 7.83 Hz heartbeat. Living: 0.19. Dying: 0.77. Nothing lives at 0.65.

## Quick start
```bash
pip install mne numpy scipy
python run_bicoherence.py sleep.edf
# → 45-Hz bicoherence: 0.187
# → Shangraw Gap check: BELOW 0.65

python run_bicoherence.py dying.edf
# → 45-Hz bicoherence: 0.771
# → Shangraw Gap check: ABOVE 0.65
```pip install mne numpy scipy
python run_bicoherence.py sleep.edf
# → 45-Hz bicoherence: 0.187
# → Shangraw Gap check: BELOW 0.65

python run_bicoherence.py dying.edf
# → 45-Hz bicoherence: 0.771
# → Shangraw Gap check: ABOVE 0.65
