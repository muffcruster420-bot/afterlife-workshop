#!/usr/bin/env python3
"""
Shangraw Gap analyzer - real 45-Hz bicoherence
Computes bicoherence for f1=15Hz, f2=30Hz (f1+f2=45Hz) in 2-sec epochs
"""
import argparse, numpy as np
import mne

def bicoherence_epoch(x, fs, f1=15, f2=30):
    n = len(x)
    win = np.hanning(n)
    X = np.fft.rfft(x * win)
    freqs = np.fft.rfftfreq(n, 1/fs)
    i1 = np.argmin(np.abs(freqs - f1))
    i2 = np.argmin(np.abs(freqs - f2))
    i3 = np.argmin(np.abs(freqs - (f1+f2)))
    num = np.abs(X[i1] * X[i2] * np.conj(X[i3]))
    den = np.sqrt((np.abs(X[i1]*X[i2])**2) * (np.abs(X[i3])**2)) + 1e-12
    return num / den

def main(edf_path, freq=45):
    raw = mne.io.read_raw_edf(edf_path, preload=True, verbose=False)
    raw.pick_types(eeg=True)
    raw.filter(1., 50., verbose=False)
    fs = raw.info['sfreq']
    data = raw.get_data()[0]

    epoch_len = int(2 * fs)
    vals = []
    for start in range(0, len(data)-epoch_len, epoch_len):
        seg = data[start:start+epoch_len]
        vals.append(bicoherence_epoch(seg, fs))

    vals = np.array(vals)
    mean_val = vals.mean()
    gap_pct = 100 * ((vals >= 0.6) & (vals <= 0.7)).mean()

    print(f"Analyzing {edf_path} at {freq} Hz")
    print(f"Living baseline expected <0.3, Dying >0.7, Gap 0.6-0.7")
    print(f"RESULT: mean={mean_val:.3f}, gap_pct={gap_pct:.1f}%")
    print(f"Epochs: {len(vals)}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--edf", required=True)
    p.add_argument("--freq", type=float, default=45)
    args = p.parse_args()
    main(args.edf, args.freq)
