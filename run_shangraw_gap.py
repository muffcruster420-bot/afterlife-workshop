#!/usr/bin/env python3
import argparse, numpy as np
import mne

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

def main(edf_path, f1, f2, window, gap_low, gap_high):
    raw = mne.io.read_raw_edf(edf_path, preload=True, verbose=False)
    raw.pick_types(eeg=True)
    fs = raw.info['sfreq']
    lpass = min(f1+f2+5, fs/2 - 0.5)
    raw.filter(1., lpass, verbose=False)
    data = raw.get_data()[0]
    epoch_len = int(window * fs)
    vals = [bicoherence_epoch(data[i:i+epoch_len], fs, f1, f2)
            for i in range(0, len(data)-epoch_len, epoch_len)]
    vals = np.array(vals)
    gap_pct = 100 * ((vals>=gap_low) & (vals<=gap_high)).mean()
    print(f"Analyzing {edf_path}")
    print(f"fs={fs}Hz, f1={f1}, f2={f2}, f3={f1+f2}, window={window}s")
    print(f"RESULT: mean={vals.mean():.3f}, gap_{gap_low}-{gap_high}={gap_pct:.2f}%, epochs={len(vals)}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--edf", required=True)
    p.add_argument("--f1", type=float, default=15)
    p.add_argument("--f2", type=float, default=30)
    p.add_argument("--window", type=float, default=2.0)
    p.add_argument("--gap-low", type=float, default=0.6)
    p.add_argument("--gap-high", type=float, default=0.7)
    args = p.parse_args()
    main(args.edf, args.f1, args.f2, args.window, args.gap_low, args.gap_high)
