import pytest, os, urllib.request
import numpy as np
import pyedflib

EDF_PATH = "data/SC4001E0-PSG.edf"
EDF_URL = "https://physionet.org/files/sleep-edfx/1.0.0/sleep-cassette/SC4001E0-PSG.edf"

def bicoherence_at(x, fs, f1, f2, nfft=4096):
    step = nfft // 2
    window = np.hanning(nfft)
    segs = []
    for i in range(0, len(x) - nfft, step):
        segs.append(x[i:i+nfft] * window)
    X = np.fft.rfft(segs, n=nfft, axis=1)
    freqs = np.fft.rfftfreq(nfft, 1/fs)
    i1 = np.argmin(np.abs(freqs - f1))
    i2 = np.argmin(np.abs(freqs - f2))
    i12 = np.argmin(np.abs(freqs - (f1+f2)))
    X1, X2, X12 = X[:, i1], X[:, i2], X[:, i12]
    B = np.mean(X1 * X2 * np.conj(X12))
    denom = np.mean(np.abs(X1*X2)**2) * np.mean(np.abs(X12)**2)
    return (np.abs(B)**2 / denom).real if denom > 0 else 0.0

def test_45hz_bicoherence():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(EDF_PATH):
        urllib.request.urlretrieve(EDF_URL, EDF_PATH)
    f = pyedflib.EdfReader(EDF_PATH)
    sig = f.readSignal(0)
    fs = f.getSampleFrequency(0)
    f.close()
    last_60s = sig[-int(60*fs):] - np.mean(sig[-int(60*fs):])
    bicoh = bicoherence_at(last_60s, fs, 22.5, 22.5)
    print(f"45Hz bicoherence (22.5+22.5): {bicoh:.3f}")
    assert 0.65 < bicoh < 0.90
