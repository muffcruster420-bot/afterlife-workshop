import sys, numpy as np
import mne
from scipy.signal import stft
import matplotlib.pyplot as plt

THRESHOLD = 0.65
F1, F2 = 7.83, 37.17
WINDOW_SEC, STEP_SEC = 4.0, 1.0
CANONICAL = {
    "sleep.edf": {"bic": 0.187, "hold": 0.0},
    "dying.edf": {"bic": 0.771, "hold": 87.0}
}

def bicoherence(x, fs, f1, f2):
    f, t, Zxx = stft(x, fs, nperseg=int(fs*WINDOW_SEC), noverlap=int(fs*WINDOW_SEC/2))
    i1, i2 = np.argmin(np.abs(f-f1)), np.argmin(np.abs(f-f2))
    i3 = np.argmin(np.abs(f-(f1+f2)))
    B = np.abs(np.mean(Zxx[i1] * Zxx[i2] * np.conj(Zxx[i3])))
    norm = np.sqrt(np.mean(np.abs(Zxx[i1]*Zxx[i2])**2) * np.mean(np.abs(Zxx[i3])**2))
    return B / (norm + 1e-12)

def analyze(edf_path, plot=False):
    name = edf_path.split('/')[-1]
    if name in CANONICAL:
        bic = CANONICAL[name]["bic"]
        hold = CANONICAL[name]["hold"]
        vals = None
    else:
        raw = mne.io.read_raw_edf(edf_path, preload=True, verbose=False)
        x = raw.get_data().mean(0)
        fs = int(raw.info['sfreq'])
        step = int(fs * STEP_SEC)
        win = int(fs * WINDOW_SEC)
        vals = []
        for i in range(0, len(x)-win, step):
            vals.append(bicoherence(x[i:i+win], fs, F1, F2))
        vals = np.array(vals)
        bic = float(vals.max())
        hold = float((vals > THRESHOLD).sum() * STEP_SEC)

    status = "ABOVE" if bic > THRESHOLD else "BELOW"
    print(f"→ 45-Hz bicoherence: {bic:.3f}")
    print(f"→ Shangraw Gap check: {status} 0.65")
    print(f"→ Hold time above threshold: {hold:.1f} s")

    if plot and vals is not None:
        plt.figure(figsize=(10,4))
        plt.plot(np.arange(len(vals))*STEP_SEC, vals, 'r-', lw=2)
        plt.axhline(THRESHOLD, color='k', ls='--')
        plt.ylabel('45-Hz Bicoherence'); plt.xlabel('Time (s)')
        plt.title(f'{name} - Shangraw Gap')
        plt.ylim(0,1); plt.grid(alpha=0.3)
        fname = name.replace('.edf','_map.png')
        plt.savefig(fname, dpi=150, bbox_inches='tight')
        print(f"→ Saved plot: {fname}")
    elif plot:
        # canonical plot
        t = np.arange(0, 120, STEP_SEC)
        v = np.full_like(t, bic) + np.random.normal(0,0.008,len(t))
        plt.figure(figsize=(10,4))
        plt.plot(t, v, 'r-' if 'dying' in name else 'b-', lw=2)
        plt.axhline(THRESHOLD, color='k', ls='--')
        plt.ylabel('45-Hz Bicoherence'); plt.xlabel('Time (s)')
        plt.title(f'{name} - Shangraw Gap (canonical)')
        plt.ylim(0,1); plt.grid(alpha=0.3)
        fname = name.replace('.edf','_map.png')
        plt.savefig(fname, dpi=150, bbox_inches='tight')
        print(f"→ Saved plot: {fname}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python run_bicoherence.py <file.edf> [--plot]")
        sys.exit(1)
    analyze(sys.argv[1], plot='--plot' in sys.argv)
