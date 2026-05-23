#!/usr/bin/env python3
import numpy as np
import pyedflib
import sys

def load_edf(filename, channel=0):
    f = pyedflib.EdfReader(filename)
    signal = f.readSignal(channel)
    fs = f.getSampleFrequency(channel)
    f.close()
    return signal, fs

def bicoherence_45hz(signal, fs):
    f1, f2 = 7.83, 37.17
    nperseg = int(4 * fs)
    step = int(fs)
    bispecs = []
    p12 = []
    p3 = []

    for start in range(0, len(signal)-nperseg, step):
        seg = signal[start:start+nperseg]
        X = np.fft.fft(seg)
        freqs = np.fft.fftfreq(len(seg), 1/fs)
        i1 = np.argmin(np.abs(freqs - f1))
        i2 = np.argmin(np.abs(freqs - f2))
        i_sum = np.argmin(np.abs(freqs - (f1+f2)))

        bispec = X[i1] * X[i2] * np.conj(X[i_sum])
        bispecs.append(bispec)
        p12.append(np.abs(X[i1] * X[i2])**2)
        p3.append(np.abs(X[i_sum])**2)

    numerator = np.abs(np.mean(bispecs))
    denominator = np.sqrt(np.mean(p12) * np.mean(p3) + 1e-12)
    bic = numerator / denominator
    return np.full(len(bispecs), bic)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_bicoherence.py <file.edf>")
        sys.exit(1)
    sig, fs = load_edf(sys.argv[1])
    bicoh = bicoherence_45hz(sig, fs)
    print(f"Mean: {np.mean(bicoh):.3f}")
    print(f"Peak: {np.max(bicoh):.3f}")
    print(f"Gap: {'ABOVE' if np.max(bicoh) > 0.65 else 'BELOW'}")
