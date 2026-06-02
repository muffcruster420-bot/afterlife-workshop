#!/usr/bin/env python3
"""
Shangraw Gap - minimal runner
Usage: python run_shangraw_gap.py --edf file.edf --freq 45
"""
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--edf', required=True)
parser.add_argument('--freq', type=float, default=45)
args = parser.parse_args()

print(f"Analyzing {args.edf} at {args.freq} Hz")
print("Living baseline expected <0.3, Dying >0.7, Gap 0.6-0.7")
print("RESULT: 0.187 (demo) — replace with real MNE bicoherence code")
