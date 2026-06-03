# Getting Started with the Shangraw Gap Analysis

This guide will help you set up and run the bicoherence analysis for the Shangraw Gap study.

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/muffcruster420-bot/afterlife-workshop.git
   cd afterlife-workshop
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Analysis

### Using Canonical Data (No EDF Files Required)

The script includes pre-computed canonical values for demonstration:

```bash
# Analyze a living (sleeping) brain — bicoherence below threshold
python run_bicoherence.py sleep.edf
# Output:
# → 45-Hz bicoherence: 0.187
# → Shangraw Gap check: BELOW 0.65
# → Hold time above threshold: 0.0 s

# Analyze a dying brain — bicoherence above threshold
python run_bicoherence.py dying.edf
# Output:
# → 45-Hz bicoherence: 0.771
# → Shangraw Gap check: ABOVE 0.65
# → Hold time above threshold: 87.0 s
```

### Using Your Own EDF Files

If you have real EDF (European Data Format) files:

1. Place your `.edf` files in the repository root
2. Run the analysis:
   ```bash
   python run_bicoherence.py your_file.edf
   ```

3. To generate a visualization:
   ```bash
   python run_bicoherence.py your_file.edf --plot
   ```

This will create a PNG plot showing the bicoherence trajectory over time.

## Understanding the Output

- **45-Hz bicoherence**: The peak coherence value between 45 Hz and 7.83 Hz frequencies
  - Living brains: ∼0.19
  - Dying brains: ∼0.77
  - Gap threshold: 0.65 (nothing stable at this value)

- **Shangraw Gap check**: Whether the peak is ABOVE or BELOW 0.65
  - BELOW: consistent with living/sleeping state
  - ABOVE: consistent with dying/transition state

- **Hold time above threshold**: Duration (in seconds) that bicoherence stayed above 0.65
  - Living: typically 0 s
  - Dying: typically 60–90 s

## Understanding the Method

- **Window size**: 4 seconds of EEG data per calculation
- **Step size**: 1-second increments (75% overlap)
- **Analysis frequencies**:
  - f1 = 7.83 Hz (Schumann fundamental resonance)
  - f2 = 45 Hz (6th harmonic of Schumann frequency)
- **Bicoherence formula**: |mean(exp(j × (φ₄₅Hz − 6 × φ₇.₈₃Hz)))|
  - Measures phase-locking coherence between the two frequencies
  - Range: 0 (no coherence) to 1 (perfect coherence)

## Obtaining EDF Files

EDF (European Data Format) is a standard format for polysomnography and EEG data. To obtain EDF files:

1. **Public databases**:
   - PhysioNet (https://physionet.org) — large collection of polysomnography and EEG datasets
   - Sleep-EDF Database (https://physionet.org/content/sleep-edfx/) — specific sleep stage data

2. **Research collaborators**: Contact the study author for access to the Kingston, Ontario dataset

3. **Your own data**: If you have sleep recording equipment (e.g., consumer EEG devices), export data to EDF format

## Troubleshooting

**ImportError: No module named 'mne'**
```bash
pip install -r requirements.txt
```

**FileNotFoundError: your_file.edf**
- Ensure the `.edf` file is in the same directory as `run_bicoherence.py`
- Check the filename for typos

**Plot not saving**
- Ensure you have write permissions in the current directory
- Check disk space

**Bicoherence values seem wrong**
- Verify the EDF file contains valid EEG data
- Ensure sample rate is correctly detected (typically 100–200 Hz for EEG)

## Study Design

See `PREREGISTRATION.md` for the formal pre-registration document, including:
- Hypotheses (n=10 dying vs n=10 living sleep)
- Falsification criteria
- Initial results (n=2 match predictions perfectly)

## Questions?

Refer to the main `README.md` for historical context and theoretical background on the Shangraw Gap, Tesla's resonance theory, and the connection to Schumann resonances.
