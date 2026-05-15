#!/usr/bin/env python3
# Shangraw Gap detector v0.2.0 - fast 0.5s steps
# Jesse Shangraw — Kingston, Ontario — May 2026
# Measures 7.83 Hz + 37.17 Hz = 45 Hz bicoherence

import sys, mne, numpy as np

F1, F2 = 7.83, 37.17 # sum = 45 Hz (6th Schumann harmonic)
FS_TARGET = 250
WIN_SEC, STEP_SEC = 4.0, 0.5
THRESHOLD = 0.65

def bicoherence(x, fs, f1, f2):
    n = len(x)
    X = np.fft.rfft(x * np.hanning(n))
    freqs = np.fft.rfftfreq(n, 1/fs)
    i1 = np.argmin(np.abs(freqs - f1))
    i2 = np.argmin(np.abs(freqs - f2))
    i3 = np.argmin(np.abs(freqs - (f1 + f2)))
    B = X[i1] * X[i2] * np.conj(X[i3])
    P1, P2, P3 = abs(X[i1])**2, abs(X[i2])**2, abs(X[i3])**2
    return abs(B)**2 / (P1 * P2 * P3 + 1e-12)

def analyze(path):
    raw = mne.io.read_raw_edf(path, preload=True, verbose=False)
    raw.pick_types(eeg=True).filter(1, 50, verbose=False).resample(FS_TARGET, verbose=False)
    data = raw.get_data().mean(0)
    w = int(WIN_SEC * FS_TARGET)
    s = int(STEP_SEC * FS_TARGET)
    vals = [bicoherence(data[i:i+w], FS_TARGET, F1, F2) for i in range(0, len(data)-w, s)]
    vals = np.array(vals)
    peak = vals.max()
    hold = (vals > THRESHOLD).sum() * STEP_SEC
    return peak, hold

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "data/sleep.edf"
    peak, hold = analyze(path)
    pred = "DYING" if hold > 10 else "LIVING"
    print(f"Peak:{peak:.3f} Time>0.65:{hold:.1f}s Pred:{pred}")
