#!/usr/bin/env python3
import argparse
import numpy as np
import pandas as pd
import mne
import os

def bicoherence_epoch(x, fs, f1, f2):
    n = len(x)
    win = np.hanning(n)
    X = np.fft.rfft(x * win)
    freqs = np.fft.rfftfreq(n, 1/fs)
    i1 = np.argmin(np.abs(freqs - f1))
    i2 = np.argmin(np.abs(freqs - f2))
    i3 = np.argmin(np.abs(freqs - (f1+f2)))
    num = np.abs(X[i1] * X[i2] * np.conj(X[i3]))
    den = np.sqrt(np.abs(X[i1]*X[i2])**2 * np.abs(X[i3])**2) + 1e-12
    return num / den

def main(edf_path, out_csv, f1, f2, window, gap_low, gap_high):
    raw = mne.io.read_raw_edf(edf_path, preload=True, verbose=False)
    raw.pick_types(eeg=True)
    fs = raw.info['sfreq']
    lpass = min(f1+f2+5, fs/2 - 0.5)
    raw.filter(1., lpass, verbose=False)
    data = raw.get_data()[0]
    epoch_len = int(window * fs)
    max_epochs = 2000
    idx = range(0, min(len(data)-epoch_len, max_epochs*epoch_len), epoch_len)
    vals = np.array([bicoherence_epoch(data[i:i+epoch_len], fs, f1, f2) for i in idx])
    epochs = np.array([data[i:i+epoch_len] for i in idx])

    os.makedirs("real_data", exist_ok=True)
    np.save("real_data/shangraw_gap_epochs.npy", epochs)
    print(f"Saved {epochs.shape[0]} epochs x {epochs.shape[1]} samples")

    gap_pct = 100 * ((vals>=gap_low) & (vals<=gap_high)).mean()
    print(f"Analyzing {edf_path}\nfs={fs}Hz, f1={f1}, f2={f2}, f3={f1+f2}, window={window}s")
    print(f"RESULT: mean={vals.mean():.3f}, gap_{gap_low}-{gap_high}={gap_pct:.2f}%, epochs={len(vals)}")

    # write results.csv for README promise
    pd.DataFrame([{
        "file": edf_path,
        "fs": fs,
        "f1": f1,
        "f2": f2,
        "f3": f1+f2,
        "window_s": window,
        "mean_bicoherence": vals.mean(),
        "gap_low": gap_low,
        "gap_high": gap_high,
        "gap_pct": gap_pct,
        "epochs": len(vals)
    }]).to_csv(out_csv, index=False)
    print(f"Wrote {out_csv}")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Shangraw Gap — 45-Hz bicoherence detector")
    p.add_argument("--file", "-f", required=True, help="Path to EDF file")
    p.add_argument("--out", "-o", default="results.csv", help="Output CSV")
    p.add_argument("--f1", type=float, default=15)
    p.add_argument("--f2", type=float, default=30)
    p.add_argument("--window", type=float, default=2.0)
    p.add_argument("--gap-low", type=float, default=0.6)
    p.add_argument("--gap-high", type=float, default=0.7)
    a = p.parse_args()
    main(a.file, a.out, a.f1, a.f2, a.window, a.gap_low, a.gap_high)
