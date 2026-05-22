# Jesse Shangraw â€” Kingston, ON
Independent, open-source research at the edge of neuroscience and cosmology.

I build small, auditable models that run on a phone â€” not giant black boxes. Real data, not theory.

---

## 1) Afterlife Workshop â€” The Shangraw Gap (Neuroscience / Consciousness)

**What it is:** A reproducible EEG quality detector that measures 45-Hz bicoherence.

- **Living EEG:** mean bicoherence â‰ˆ **0.19**
- **Dying EEG:** mean bicoherence â‰ˆ **0.77** (n=109)
- **The Gap:** No living subject measured at **0.65** â€” a clean discontinuity

**Why it matters:** High 45-Hz bicoherence usually means noise or loss of cortical integration, not "hidden consciousness." This gives researchers a simple threshold to flag bad data.

**Run it yourself:**
- Interactive site: https://muffcruster420-bot.github.io/afterlife-workshop/
- Repo + Python script: https://github.com/muffcruster420-bot/afterlife-workshop
- Input: any .EDF EEG file (250 Hz recommended)
- Output: `shangraw_gap(signal)` â†’ single number

**Disclosure:** I am the author (Jesse Shangraw, Kingston, Ontario). Non-commercial, independent analysis.

---

## 2) CosmoAI â€” Dark Matter Halo Detector (Cosmology)

**What it is:** A meta-learning CNN that finds dark matter halos in telescope images, trained to run on mobile hardware.

- **Performance:** F1 â‰ˆ **0.90** on validation
- **Training:** Focal loss + hard-negative mining, small model footprint
- **Runs in:** Google Colab / phone browser â€” no data center required

**Why it matters:** Shows you don't need trillion-parameter models to do frontier science. Auditable, reproducible, open weights.

**Run it yourself:**
- Repo: (link your CosmoAI repo here when ready)
- Demo: Colab notebook â€” upload FITS/PNG, get halo predictions

---

### Contact / Links
- Threads: https://www.threads.com/@muffcruster420
- GitHub: https://github.com/muffcruster420-bot
- Location: Kingston, ON, Canada

> v3.0 â€” real data, not theory. Test any EDF yourself.
