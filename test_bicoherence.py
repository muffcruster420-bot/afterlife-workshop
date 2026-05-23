import numpy as np
from run_bicoherence import bicoherence_45hz

def test_living_gap():
    fs = 256
    t = np.arange(0, 300, 1/fs)
    living = np.random.randn(len(t))
    mean_living = np.mean(bicoherence_45hz(living, fs))
    print(f"Living mean: {mean_living:.3f} (target ~0.19)")
    assert mean_living < 0.35, f"FAILED: {mean_living:.3f}"

def test_dying_gap():
    fs = 256
    t = np.arange(0, 300, 1/fs)
    # Real Shangraw coupling: 7.83 + 37.17 = 45
    s1 = np.cos(2*np.pi*7.83*t)
    s2 = np.cos(2*np.pi*37.17*t)
    s3 = np.cos(2*np.pi*45*t + np.random.randn(len(t))*0.1)
    dying = s1 + s2 + s3
    mean_dying = np.mean(bicoherence_45hz(dying, fs))
    print(f"Dying mean: {mean_dying:.3f} (target ~0.77)")
    assert mean_dying > 0.60, f"FAILED: {mean_dying:.3f}"
