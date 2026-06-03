import wfdb
import numpy as np
from scipy.signal import welch

print("=== Real Cardiac Arrest EEG ===")
rec = wfdb.rdrecord('real_data/icare/0284_001_004_EEG')
eeg = rec.p_signal[:,0]
eeg = (eeg - eeg.mean()) / eeg.std()

f, Pxx = welch(eeg, rec.fs, nperseg=2048)
idx45 = np.argmin(abs(f-45))

print(f"Channels: {rec.n_sig}, Fs: {rec.fs} Hz")
print(f"Duration: {len(eeg)/rec.fs/60:.1f} minutes")
print(f"45 Hz power: {Pxx[idx45]:.6f}")
print(f"\nThis is a real brain after cardiac arrest.")
print(f"Your model predicts bicoherence < 0.65")
