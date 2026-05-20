import mne
import numpy as np
from scipy.signal import hilbert, butter, filtfilt
import matplotlib.pyplot as plt

raw = mne.io.read_raw_edf('sleep.edf', preload=True, verbose=False)
sfreq = raw.info['sfreq']
eeg = raw.get_data(picks='EEG Fpz-Cz')[0]
nyq = sfreq / 2

b_theta, a_theta = butter(4, [4/nyq, 8/nyq], btype='band')
theta = filtfilt(b_theta, a_theta, eeg)
theta_phase = np.angle(hilbert(theta))

b_gamma, a_gamma = butter(4, [30/nyq, 45/nyq], btype='band')
gamma = filtfilt(b_gamma, a_gamma, eeg)
gamma_amp = np.abs(hilbert(gamma))

pac = np.abs(np.mean(gamma_amp * np.exp(1j * theta_phase)))
print(f"Sampling rate: {sfreq} Hz")
print(f"Theta-gamma PAC (MI): {pac:.4f}")

plt.figure(figsize=(8,4))
plt.hist(theta_phase, bins=18, weights=gamma_amp, density=True)
plt.title(f'Sleep PAC: MI = {pac:.4f}')
plt.xlabel('Theta phase'); plt.ylabel('Gamma amplitude')
plt.savefig('sleep_pac.png', dpi=150)
print("Saved sleep_pac.png")
