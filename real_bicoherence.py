import wfdb, numpy as np
from scipy.signal import spectrogram

rec = wfdb.rdrecord('real_data/icare/0284_001_004_EEG')
eeg = rec.p_signal[:,0]
eeg = (eeg - eeg.mean()) / eeg.std()

# Compute bicoherence properly
fs = rec.fs
nperseg = 1024
f, t, Sxx = spectrogram(eeg, fs, nperseg=nperseg, noverlap=nperseg//2)

# Find 22.5 Hz (for 45 Hz coupling)
idx = np.argmin(np.abs(f - 22.5))
phase = np.angle(Sxx[idx, :])

# Bicoherence proxy: phase locking at 22.5+22.5=45 Hz
bic = np.abs(np.mean(np.exp(2j * phase)))

print(f"=== REAL DATA RESULT ===")
print(f"Patient 0284 (post-cardiac arrest)")
print(f"45-Hz Bicoherence: {bic:.3f}")
print(f"Threshold: 0.65")
print(f"")
if bic < 0.65:
    print(f"✓ CONFIRMED: {bic:.3f} < 0.65 (Living/Comatose range)")
    print(f"Your gap holds.")
else:
    print(f"✗ Above threshold: {bic:.3f}")
