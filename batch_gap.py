#!/usr/bin/env python3
import subprocess, glob, os, re, csv
from pathlib import Path

# folders to scan — add more as you download
folders = [
    "real_data",
    "data/awake",
    "data/anesthesia",
    "data",
]

edfs = []
for f in folders:
    edfs += glob.glob(f"{f}/**/*.edf", recursive=True)

print(f"Found {len(edfs)} EDF files")
results = []

for edf in sorted(edfs):
    print(f"\n=== {edf} ===")
    try:
        out = subprocess.check_output(
            ["python", "run_shangraw_gap.py", "--edf", edf],
            stderr=subprocess.STDOUT, text=True, timeout=300
        )
        # parse RESULT line like: RESULT: mean=0.806, gap_pct=10.0%
        m = re.search(r"RESULT: mean=([0-9.]+), gap_pct=([0-9.]+)%", out)
        epochs = re.search(r"Epochs: (\d+)", out)
        mean = float(m.group(1)) if m else None
        gap = float(m.group(2)) if m else None
        ep = int(epochs.group(1)) if epochs else None
        results.append({"file": edf, "mean": mean, "gap_pct": gap, "epochs": ep})
        print(f"  -> mean={mean}, gap={gap}%, epochs={ep}")
    except Exception as e:
        print(f"  FAILED: {e}")
        results.append({"file": edf, "mean": None, "gap_pct": None, "epochs": None})

# write csv
os.makedirs("results", exist_ok=True)
with open("results/batch_results.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["file","mean","gap_pct","epochs"])
    w.writeheader()
    w.writerows(results)

# update gap_summary.txt
with open("results/gap_summary.txt", "w") as f:
    f.write("Shangraw Gap batch run\n")
    for r in results:
        if r["mean"] is not None:
            f.write(f"{r['file']}: mean={r['mean']}, gap_pct={r['gap_pct']}%, epochs={r['epochs']}\n")

print("\nDone. See results/batch_results.csv")
