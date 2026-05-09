import mne, numpy as np, sys
from scipy.signal import hilbert

def bicoherence_45hz(eeg, fs):
    f = np.fft.rfftfreq(len(eeg), 1/fs); X = np.fft.rfft(eeg)
    i45 = np.argmin(abs(f-45)); i90 = np.argmin(abs(f-90))
    bispec = X[i45]*X[i45]*np.conj(X[i90])
    return abs(bispec)/(abs(X[i45])**2*abs(X[i90])+1e-12)

def schumann_plv(eeg, fs, f0=7.83):
    phase = np.angle(hilbert(eeg)); t = np.arange(len(eeg))/fs
    return abs(np.mean(np.exp(1j*(phase-2*np.pi*f0*t))))

if __name__ == "__main__":
    raw = mne.io.read_raw_edf(sys.argv[1], preload=True, verbose=False)
    eeg = raw.get_data(picks='eeg')[0]; fs = raw.info['sfreq']
    bic = bicoherence_45hz(eeg, fs); plv = schumann_plv(eeg, fs)
    print(f"45-Hz bicoherence: {bic:.3f}")
    print(f"Schumann PLV: {plv:.3f}")
    print(f"Shangraw Gap check: {'BELOW 0.65' if bic<0.65 else 'ABOVE 0.65'}")