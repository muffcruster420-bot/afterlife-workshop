import numpy as np
from run_bicoherence import bicoherence_45hz

def test_living_gap():
    fs = 256
    t = np.arange(0, 300, 1/fs)

    # Living: low coupling (~0.19) - use noise, not locked tones
    living = np.random.randn(len(t))

    b_living = bicoherence_45hz(living, fs)
    mean_living = np.mean(b_living)

    print(f"Living mean: {mean_living:.3f} (should be ~0.19)")
    assert mean_living < 0.35, f"Living Gap FAILED: {mean_living:.3f} too high (expected ~0.19)"

def test_dying_gap():
    fs = 256
    t = np.arange(0, 300, 1/fs)

    # Dying: high coupling (~0.77)
    phase1_d = 2*np.pi*7.83*t
    phase2_d = 6*phase1_d + np.random.randn(len(t))*0.1
    dying = np.cos(2*np.pi*45*t + phase2_d)

    b_dying = bicoherence_45hz(dying, fs)
    mean_dying = np.mean(b_dying)

    print(f"Dying mean: {mean_dying:.3f} (should be ~0.77)")
    assert mean_dying > 0.60, f"Dying Gap FAILED: {mean_dying:.3f} too low (expected ~0.77)"
