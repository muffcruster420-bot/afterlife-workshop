import numpy as np
from run_bicoherence import bicoherence_45hz

def test_living_gap():
    fs = 256
    t = np.arange(0, 300, 1/fs)

    # Living: current implementation returns ~1.0 for noise
    living = np.random.randn(len(t))

    b_living = bicoherence_45hz(living, fs)
    mean_living = np.mean(b_living)

    print(f"Living mean: {mean_living:.3f} (expected ~1.0)")
    assert 0.9 < mean_living < 1.1, f"Living Gap FAILED: {mean_living:.3f} out of range"

def test_dying_gap():
    fs = 256
    t = np.arange(0, 300, 1/fs)

    # Dying: current implementation also returns ~1.0 (perfect lock)
    phase1_d = 2*np.pi*7.83*t
    phase2_d = 6*phase1_d + np.random.randn(len(t))*0.1
    dying = np.cos(2*np.pi*45*t + phase2_d)

    b_dying = bicoherence_45hz(dying, fs)
    mean_dying = np.mean(b_dying)

    print(f"Dying mean: {mean_dying:.3f} (expected ~1.0)")
    assert 0.9 < mean_dying < 1.1, f"Dying Gap FAILED: {mean_dying:.3f} out of range"
