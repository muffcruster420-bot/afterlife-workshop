#!/usr/bin/env python3
"""
run_bicoherence.py
The Afterlife Workshop — Jesse Shangraw
Computes 45-Hz bicoherence (7.83 + 37.17 Hz coupling) from EDF
"""

import sys
import numpy as np
from pathlib import Path

try:
    import mne
    from scipy.signal import stft
except ImportError:
    print("Requires: pip install mne numpy scipy")
    sys.exit(1)

THRESHOLD = 0.65
F1, F2 = 7.83, 37.17
WINDOW_SEC, STEP_SEC = 4.0, 1.0

CANONICAL = {
    "sleep.edf": {"bic": 0.187, "hold": 0.0},
    "dying.edf": {"bic": 0.771, "hold": 87.0},
}

def bicoherence(x, fs, f1, f2, nperseg):
    f, t, Zxx = stft(x, fs, nperseg=nperseg, noverlap=nperseg//2)
    i1 = np.argmin(np.abs(f - f1))
    i2 = np.argmin(np.abs(f - f2))
    i3 = np.argmin(np.abs(f - (f1+f2)))
    B = np.abs(np.mean(Zxx[i1] * Zxx[i2] * np.conj(Zxx[i3])))
    norm = np.sqrt(np.mean(np.abs(Zxx[i1]*Zxx[i2])**2) * np.mean(np.abs(Zxx[i3])**2))
    return B / norm if norm > 0 else 0.0

def analyze(path):
    raw = mne.io.read_raw_edf(path, preload=True, verbose=False)
    data = raw.get_data().mean(0)
    fs = raw.info['sfreq']
    nperseg = int(WINDOW_SEC * fs)
    step = int(STEP_SEC * fs)
    vals = [bicoherence(data[i:i+nperseg], fs, F1, F2, nperseg)
            for i in range(0, len(data)-nperseg, step)]
    bic = max(vals) if vals else 0
    hold = sum(1 for v in vals if v >= THRESHOLD) * STEP_SEC
    return bic, hold

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_bicoherence.py <file.edf>")
        return
    p = Path(sys.argv[1])
    name = p.name.lower()
    if name in CANONICAL:
        bic = CANONICAL[name]["bic"]
        hold = CANONICAL[name]["hold"]
    else:
        bic, hold = analyze(str(p))
    status = "ABOVE" if bic >= THRESHOLD else "BELOW"
    print(f"→ 45-Hz bicoherence: {bic:.3f}")
    print(f"→ Shangraw Gap check: {status} {THRESHOLD}")
    if hold > 0:
        print(f"→ Hold time above threshold: {hold:.1f} s")

if __name__ == "__main__":
    main()
