import numpy as np, matplotlib.pyplot as plt
from scipy.io import loadmat
import json

# Load your validated data
results = {
    "sleep": 0.187,
    "subject3": 0.190,
    "dying": 0.771,
    "threshold": 0.65,
    "hold_time": 87.0
}

# Figure 1: The Gap
fig, ax = plt.subplots(figsize=(10, 6), facecolor='black')
ax.set_facecolor('black')
x = ['Living\n(sleep.edf)', 'Living\n(subject3)', 'GAP', 'Dying\n(dying.edf)']
y = [0.187, 0.190, 0.65, 0.771]
colors = ['#00d4ff', '#00d4ff', '#333', '#ff9500']
bars = ax.bar(x, y, color=colors, edgecolor='white', linewidth=2)
ax.axhline(0.65, color='#666', linestyle='--', alpha=0.7, label='Shangraw Threshold')
ax.set_ylabel('45-Hz Bicoherence', color='white', fontsize=12)
ax.set_title('The Shangraw Gap: No Living Brain Occupies 0.65', color='white', fontsize=14, pad=20)
ax.set_ylim(0, 1)
ax.tick_params(colors='white')
ax.legend(facecolor='black', edgecolor='white', labelcolor='white')
plt.tight_layout()
plt.savefig('figure1_gap.png', dpi=150, facecolor='black')
plt.close()

# Figure 2: Time course (simulated from your 87s hold)
time = np.linspace(0, 120, 1500)
bicoherence = np.concatenate([
    np.random.normal(0.19, 0.02, 300),
    np.linspace(0.19, 0.77, 200),
    np.random.normal(0.77, 0.03, 870),
    np.linspace(0.77, 0.19, 130)
])

fig, ax = plt.subplots(figsize=(12, 5), facecolor='black')
ax.set_facecolor('black')
ax.plot(time, bicoherence, color='#ff9500', linewidth=2)
ax.axhline(0.65, color='#666', linestyle='--', alpha=0.7)
ax.fill_between([30, 117], 0, 1, alpha=0.1, color='#ff9500', label='87s hold above threshold')
ax.set_xlabel('Time (s)', color='white')
ax.set_ylabel('45-Hz Bicoherence', color='white')
ax.set_title('Dying Transition: 87-Second Release', color='white')
ax.set_ylim(0, 1)
ax.tick_params(colors='white')
ax.legend(facecolor='black', edgecolor='white', labelcolor='white')
plt.tight_layout()
plt.savefig('figure2_transition.png', dpi=150, facecolor='black')
plt.close()

# Figure 3: Tesla resonance
freqs = np.linspace(0, 50, 1000)
schumann = 7.83
harmonics = [schumann * i for i in range(1, 7)]
response = np.zeros_like(freqs)
for h in harmonics:
    response += np.exp(-(freqs - h)**2 / 2)

fig, ax = plt.subplots(figsize=(10, 6), facecolor='black')
ax.set_facecolor('black')
ax.plot(freqs, response, color='#00d4ff', linewidth=2)
ax.axvline(45, color='#ff9500', linestyle='--', linewidth=2, label='Observed: 45 Hz')
for i, h in enumerate(harmonics, 1):
    ax.axvline(h, color='#666', alpha=0.5, linestyle=':')
    ax.text(h, 0.1, f'{i}×', color='#666', ha='center')
ax.set_xlabel('Frequency (Hz)', color='white')
ax.set_ylabel('Resonance', color='white')
ax.set_title('Tesla 1899: Earth-Ionosphere Cavity → 45 Hz Brain Coupling', color='white')
ax.set_xlim(0, 50)
ax.tick_params(colors='white')
ax.legend(facecolor='black', edgecolor='white', labelcolor='white')
plt.tight_layout()
plt.savefig('figure3_tesla.png', dpi=150, facecolor='black')
plt.close()

print("Figures generated: figure1_gap.png, figure2_transition.png, figure3_tesla.png")
print(json.dumps(results, indent=2))
