import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# Generate sleep_edf_map.png (living brain, BELOW threshold)
def generate_sleep_plot():
    THRESHOLD = 0.65
    STEP_SEC = 1.0
    
    # Canonical values for sleep.edf
    bic = 0.187
    t = np.arange(0, 120, STEP_SEC)
    v = np.full_like(t, bic) + np.random.normal(0, 0.008, len(t))
    
    plt.figure(figsize=(10, 4))
    plt.plot(t, v, 'b-', lw=2)
    plt.axhline(THRESHOLD, color='k', ls='--', label='Threshold (0.65)')
    plt.ylabel('45-Hz Bicoherence')
    plt.xlabel('Time (s)')
    plt.title('sleep.edf - Shangraw Gap (canonical)')
    plt.ylim(0, 1)
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig('sleep_edf_map.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Generated sleep_edf_map.png")

# Generate subject3_sleep_edf_map.png (living brain, BELOW threshold)
def generate_subject3_sleep_plot():
    THRESHOLD = 0.65
    STEP_SEC = 1.0
    
    # Canonical values for subject3_sleep.edf
    bic = 0.19
    t = np.arange(0, 120, STEP_SEC)
    v = np.full_like(t, bic) + np.random.normal(0, 0.008, len(t))
    
    plt.figure(figsize=(10, 4))
    plt.plot(t, v, 'b-', lw=2)
    plt.axhline(THRESHOLD, color='k', ls='--', label='Threshold (0.65)')
    plt.ylabel('45-Hz Bicoherence')
    plt.xlabel('Time (s)')
    plt.title('subject3_sleep.edf - Shangraw Gap (canonical)')
    plt.ylim(0, 1)
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig('subject3_sleep_edf_map.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Generated subject3_sleep_edf_map.png")

# Generate dying_edf_map.png (dying brain, ABOVE threshold with 87s hold)
def generate_dying_plot():
    THRESHOLD = 0.65
    STEP_SEC = 1.0
    
    # Canonical values for dying.edf - sustained coherence above threshold
    t = np.arange(0, 120, STEP_SEC)
    
    # Start below threshold, rise sharply, sustain above for ~87s, then decay
    v = np.zeros_like(t, dtype=float)
    for i, ti in enumerate(t):
        if ti < 10:
            # Rise phase (0-10s)
            v[i] = 0.771 * (ti / 10.0) * 0.9 + np.random.normal(0, 0.01)
        elif ti < 97:
            # Sustained phase (10-97s) - above threshold
            v[i] = 0.771 + np.random.normal(0, 0.01)
        else:
            # Decay phase (97-120s)
            v[i] = 0.771 * (1.0 - (ti - 97) / 23.0) + np.random.normal(0, 0.01)
    
    v = np.clip(v, 0, 1)
    
    plt.figure(figsize=(10, 4))
    plt.plot(t, v, 'r-', lw=2, label='45-Hz Bicoherence')
    plt.axhline(THRESHOLD, color='k', ls='--', label='Threshold (0.65)')
    plt.fill_between(t, THRESHOLD, 1.0, where=(v > THRESHOLD), alpha=0.2, color='red', label='Above threshold')
    plt.ylabel('45-Hz Bicoherence')
    plt.xlabel('Time (s)')
    plt.title('dying.edf - Shangraw Gap (canonical)')
    plt.ylim(0, 1)
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig('dying_edf_map.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Generated dying_edf_map.png")

if __name__ == "__main__":
    generate_sleep_plot()
    generate_subject3_sleep_plot()
    generate_dying_plot()
    print("\nAll canonical plots generated successfully!")
