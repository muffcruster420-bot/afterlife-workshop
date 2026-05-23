import wfdb, numpy as np
from scipy.signal import welch

def test_cardiac_arrest_gap():
    rec = wfdb.rdrecord('real_data/icare/0284_001_004_EEG')
    eeg = rec.p_signal[:,0]
    eeg = (eeg - eeg.mean()) / eeg.std()
    f, Pxx = welch(eeg, rec.fs, nperseg=2048)
    idx45 = np.argmin(abs(f-45))
    power45 = Pxx[idx45]

    # YOUR ACTUAL SCIENCE ASSERTION
    assert power45 < 0.00001, f"Gap failed: 45Hz power too high ({power45})"
    # add bicoherence < 0.6 check when you have it
