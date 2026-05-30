# Shangraw Gap (PAC = 0.65)

**Definition:** The Shangraw Gap is the phase transition in phase-amplitude coupling that separates unconscious sleep (PAC < 0.65) from organized activity in the dying human brain (PAC > 0.65).

**First described:** May 18, 2026 by Jesse Shangraw, Kingston, Ontario
**Archived:** May 20, 2026 — DOI: 10.5281/zenodo.20466962

> YOU CROSS THE GAP!! YOU NEVER COME BACK!!!!!

Dying EEG: PAC = 0.771
Sleep EEG: PAC = 0.187
📖 Docs: https://github.com/muffcruster420-bot/afterlife-workshop/wiki
# The Shangraw Gap - 45-Hz Bicoherence in Living vs Dying EEG
> **→ Got data? Post your numbers in [Issue #1 - Break the Gap](https://github.com/muffcruster420-bot/afterlife-workshop/issues/1)**
Open EDF analysis from Kingston, Ontario. Built 100% on a phone. No lab, no funding.

> Living brains sit near 0.19. Dying brains jump near 0.77. Almost nothing lands between 0.6 and 0.7.

This repo is not a paper. It is a testable claim with code and data.

---

## The Claim (falsifiable)

For standard 10-20 EEG analyzed in 2-second epochs at 45 Hz:

1. **Living baseline** bicoherence clusters **below 0.3**
2. **Peri-arrest / dying** bicoherence clusters **above 0.7**
3. **The Gap (0.6 to 0.7)** contains **<5% of all epochs**

Find one counterexample and the claim breaks.

## Try to Break It

1. Clone this repo
2. Run:
   ```bash
   python run_shangraw_gap.py --edf yourfile.edf --freq 45
   ```
3. Post the output in Issues with the tag `replication`

If your file shows >10% of epochs in 0.6-0.7, or a dying brain <0.5, I will add your result to the table below and credit you.

## What I Found So Far

| Dataset | Location | Condition | Mean 45-Hz Bicoherence | % Epochs in Gap (0.6-0.7) | Source |
| --- | --- | --- | --- | --- | --- |
| Kingston-01 | Kingston, ON | Living baseline | 0.187 | 0.0% | included in /data |
| Kingston-01 | Kingston, ON | Post-arrest | 0.771 | 0.0% | included in /data |

*n = 1 so far. This is why I need your help.*

## Data

All data is EDF format, 10-20 montage preferred.

**Included:**
- `/data/kingston_baseline.edf` and `/data/kingston_postarrest.edf` - my original recordings

**Public sets to test:**
1. **CHB-MIT Scalp EEG Database (living)**
   - PhysioNet, 22 subjects, free download
   - https://physionet.org/content/chbmit/1.0.0/
   - Suggested file: `chb01_03.edf` (interictal segment)

2. **Vicente et al. 2022 - Dying Human Brain (dying)**
   - 900 s continuous EEG during cardiac arrest, 87-year-old male
   - Paper: https://doi.org/10.3389/fnagi.2022.813531
   - Data: included in Supplementary Material, or request EDF from corresponding author ajmal.zemmar@gmail.com

Add your own EDF and open a PR to the table.

## How to Run

Requirements: Python 3.9+, numpy, scipy, mne

```bash
pip install -r requirements.txt
python run_shangraw_gap.py --edf data/kingston_baseline.edf --freq 45 --window 2
```

Output:
```
mean_bicoherence: 0.187
gap_percent: 0.0
epochs_analyzed: 450
```

## Method (short)

- Notch filter 60 Hz and harmonics
- Hamming window, 2 s epochs, 1 s overlap
- FFT -> bispectrum -> bicoherence at target frequency
- No manual threshold tuning

Full code in `run_shangraw_gap.py`. Read it, fork it, break it.

## Why This Format

I got 1,500+ clones and zero replications. Comments are easy. Running code is hard. This README makes the hard part the only part that counts.

## Contact

Jesse Shangraw - Kingston, Ontario
Open an Issue for replications. I respond to data, not debates.

## License

MIT - use it, break it, cite it.

---
*Built on mobile, May 2026. If you replicate on a phone too, tell me.*
