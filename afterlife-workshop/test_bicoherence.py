import pytest
import numpy as np
import pyedflib
from scipy.signal import welch

EDF_PATH = "data/SC4001E0-PSG.edf"

def test_imports():
    import wfdb, scipy
    assert wfdb.__version__

def test_45hz_power():
    """Load EDF, check 45 Hz power in final 60s (your May 19 finding)"""
    f = pyedflib.EdfReader(EDF_PATH)
    sig = f.readSignal(0)
    fs = f.getSampleFrequency(0)
    f.close()

    last_60s = sig[-int(60*fs):]
    freqs, psd = welch(last_60s, fs=fs, nperseg=4096)
    idx_45 = np.argmin(np.abs(freqs - 45))
    power_45hz = psd[idx_45] / np.max(psd)

    assert 0.5 < power_45hz < 0.95, f"45Hz power {power_45hz:.3f} out of range"
