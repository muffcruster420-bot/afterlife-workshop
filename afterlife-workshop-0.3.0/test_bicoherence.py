import numpy as np
from run_bicoherence import bicoherence_45hz

# Generate fake 45-Hz signal with 7.83 Hz coupling
fs = 256
t = np.arange(0, 300, 1/fs)

# Living: low coupling (~0.19)
phase1 = 2*np.pi*7.83*t + np.random.randn(len(t))*0.5
phase2 = 6*phase1 + np.random.randn(len(t))*2.0
living = np.cos(2*np.pi*45*t + phase2)

# Dying: high coupling (~0.77)
phase1_d = 2*np.pi*7.83*t
phase2_d = 6*phase1_d + np.random.randn(len(t))*0.1
dying = np.cos(2*np.pi*45*t + phase2_d)

print("Testing living (should be ~0.19):")
b_living = bicoherence_45hz(living, fs)
print(f"Mean: {np.mean(b_living):.3f}, Peak: {np.max(b_living):.3f}")

print("\nTesting dying (should be ~0.77):")
b_dying = bicoherence_45hz(dying, fs)
print(f"Mean: {np.mean(b_dying):.3f}, Peak: {np.max(b_dying):.3f}")
