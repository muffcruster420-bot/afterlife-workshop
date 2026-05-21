# run_shangraw_gap.py
# The Shangraw Gap Detector v0.3.0

import sys
from analyze_transition import detect_gap

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_shangraw_gap.py <file.edf>")
        return
    path = sys.argv[1]
    score = detect_gap(path)
    print(f"\nBicoherence = {score:.3f}")
    print(f"Living ~0.19 | Threshold 0.65 | Dying ~0.77")
    print(">>> ABOVE" if score > 0.65 else ">>> BELOW")

if __name__ == "__main__":
    main()
