import os, pandas as pd
from src.shangraw_gap import shangraw_gap

path = 'real_data'
files = [f for f in os.listdir(path) if f.endswith('.csv') or f.endswith('.txt')] if os.path.exists(path) else []
if not files:
    print('Add your OpenBCI file to real_data/ folder first')
else:
    f = os.path.join(path, files[0])
    df = pd.read_csv(f, comment='%')
    col =
cat > README.md << 'EOF'
# Afterlife Workshop

EEG bicoherence mapping of consciousness transitions — NDEs, terminal EEG, RHI hypnosis, and altered states.

Built entirely on mobile by Jesse Shangraw (Kingston, ON).

## The Shangraw Gap

A simple, robust detector for mains noise and poor grounding.

**Validated 2026-05-21 on phone in Google Colab:**
- GOOD synthetic EEG: **Gap = 1.23**
- POOR synthetic EEG with 45Hz added: **Gap = 135.72**

## Usage
```python
from src.shangraw_gap import shangraw_gap
gap = shangraw_gap(eeg_signal, fs=250, target=45)
