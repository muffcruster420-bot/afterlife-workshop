import numpy as np
from run_bicoherence import bicoherence_45hz
import os
from scipy.io import loadmat

def test_living_gap():
    fs = 256
    t = np.arange(0, 300, 1/fs)
    living = np.random.randn(len(t))
    mean_living = np.mean(bicoherence_45hz(living, fs))
    print(f"Living mean: {mean_living:.3f} (target ~0.19)")
    assert mean_living < 0.35

def test_dying_gap():
    fs = 256
    t = np.arange(0, 300, 1/fs)
    s1 = np.cos(2*np.pi*7.83*t)
    s2 = np.cos(2*np.pi*37.17*t)
    s3 = np.cos(2*np.pi*45*t + np.random.randn(len(t))*0.1)
    dying = s1 + s2 + s3
    mean_dying = np.mean(bicoherence_45hz(dying, fs))
    print(f"Dying mean: {mean_dying:.3f} (target ~0.77)")
    assert mean_dying > 0.60

def test_real_0284():
    path = 'real_data/icare/0284_001_004_EEG.mat'
    mat = loadmat(path)
    sig = None
    for key in ['val', 'data', 'signal', 'EEG']:
        if key in mat:
            sig = mat[key].squeeze()
            break
    if sig is None:
        sig = max([v for v in mat.values() if hasattr(v, 'size')], key=lambda x: x.size).squeeze()

    fs = 256
    data = sig[:fs*300] if len(sig) > fs*300 else sig
    bico = bicoherence_45hz(data, fs)
    mean_real = np.mean(bico)

    print(f"=== REAL 0284 RESULT ===")
    print(f"Mean bicoherence: {mean_real:.3f}")
    print(f"Peak: {np.max(bico):.3f}")
    print(f"Classification: {'DYING (>0.65)' if mean_real > 0.65 else 'LIVING (<0.65)'}")
