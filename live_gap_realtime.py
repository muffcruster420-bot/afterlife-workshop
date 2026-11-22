#!/usr/bin/env python3
"""
Shangraw Gap - Live EDF Real-Time Runner
All they have to do: download an EDF, run it, watch the status.

Usage:
  python live_gap_realtime.py --file your_file.edf
  python live_gap_realtime.py --file your_file.edf --window 2.0 --speed 1.0
"""
import argparse, json, time, sys
import numpy as np
import pandas as pd
try:
    import mne
except ImportError:
    print("Need mne: pip install mne")
    sys.exit(1)

def bicoherence_epoch(x, fs, f1, f2):
    n = len(x)
    win = np.hanning(n)
    X = np.fft.rfft(x * win)
    freqs = np.fft.rfftfreq(n, 1/fs)
    i1 = np.argmin(np.abs(freqs - f1))
    i2 = np.argmin(np.abs(freqs - f2))
    i3 = np.argmin(np.abs(freqs - (f1+f2)))
    num = np.abs(X[i1] * X[i2] * np.conj(X[i3]))
    den = np.sqrt(np.abs(X[i1]*X[i2])**2 * np.abs(X[i3])**2 + 1e-12)
    return float(num / den)

def status_for(val, lock_streak):
    if lock_streak >= 3:
        return "DYING LOCKED"
    if 0.60 <= val <= 0.70:
        return "GAP TOUCH - TRANSIENT"
    if val >= 0.71:
        return "APPROACHING LOCK"
    if val < 0.12:
        return "DEEP SLEEP"
    return "LIVING AWAKE"

def main():
    p = argparse.ArgumentParser(description="Shangraw Gap - Live EDF Real-Time")
    p.add_argument("--file", "-f", required=True, help="Path to EDF file")
    p.add_argument("--f1", type=float, default=15)
    p.add_argument("--f2", type=float, default=30)
    p.add_argument("--window", type=float, default=2.0)
    p.add_argument("--speed", type=float, default=1.0)
    p.add_argument("--out-json", default="live_gap.json")
    p.add_argument("--out-csv", default="live_gap.csv")
    a = p.parse_args()
    print(f"Loading {a.file} ...")
    raw = mne.io.read_raw_edf(a.file, preload=True, verbose=False)
    raw.pick_types(eeg=True)
    fs = float(raw.info['sfreq'])
    lpass = min(a.f1 + a.f2 + 5, fs/2 - 0.5)
    raw.filter(1., lpass, verbose=False)
    data = raw.get_data()[0]
    print(f"fs={fs}Hz, f1={a.f1}, f2={a.f2}, f3={a.f1+a.f2}, window={a.window}s")
    print("Starting live readout. Press Ctrl+C to stop.\n")
    print("TIME     EPOCH  BICOH  STATUS")
    print("-----------------------------------")
    epoch_len = int(a.window * fs)
    history = []
    lock_streak = 0
    start = time.time()
    for epoch_idx, start_sample in enumerate(range(0, len(data)-epoch_len, epoch_len)):
        seg = data[start_sample:start_sample+epoch_len]
        val = bicoherence_epoch(seg, fs, a.f1, a.f2)
        if val >= 0.77:
            lock_streak += 1
        elif val < 0.70:
            lock_streak = 0
        status = status_for(val, lock_streak)
        elapsed = epoch_idx * a.window
        mm = int(elapsed // 60)
        ss = int(elapsed % 60)
        print(f"{mm:02d}:{ss:02d}   {epoch_idx+1:4d}   {val:.3f}  {status}")
        history.append({"epoch": epoch_idx+1, "time_s": elapsed, "bicoherence": val, "status": status})
        live = {
            "file": a.file, "fs": fs, "f1": a.f1, "f2": a.f2, "f3": a.f1+a.f2,
            "window_s": a.window, "epoch": epoch_idx+1, "time_s": elapsed,
            "bicoherence": val, "status": status, "lock_streak": lock_streak,
            "history": history[-120:], "gap_low": 0.60, "gap_high": 0.70,
            "updated": time.strftime("%H:%M:%S")
        }
        with open(a.out_json, "w") as f:
            json.dump(live, f, indent=2)
        pd.DataFrame(history).to_csv(a.out_csv, index=False)
        if a.speed > 0:
            target = (epoch_idx+1) * a.window / a.speed
            spent = time.time() - start
            sleep_for = target - spent
            if sleep_for > 0:
                time.sleep(sleep_for)
    print(f"\nDone. Wrote {a.out_json} and {a.out_csv} with {len(history)} epochs.")
    if history:
        vals = [h["bicoherence"] for h in history]
        gap_pct = 100 * sum(1 for v in vals if 0.60 <= v <= 0.70) / len(vals)
        print(f"Mean={np.mean(vals):.3f}, Gap 0.60-0.70={gap_pct:.2f}%, Max={max(vals):.3f}")

if __name__ == "__main__":
    main()
