import pandas as pd

df = pd.read_csv('subjects_metadata.csv')
print("Columns:", df.columns.tolist())

# --- PHENOTYPE FILTER (works with current CSV) ---
# For now, search 'notes' and 'type' for keywords
# When the 607 arrives, just add real icd10/ketamine columns
notes = df['notes'].fillna('').str.lower()
type_col = df['type'].fillna('').str.lower()

dangerous_mask = (
    notes.str.contains('g40.9|g93.4|ketamine|epilepsy|encephalopathy') |
    type_col.str.contains('seizure|status|ketamine')
)

dangerous_cohort = df[dangerous_mask]

print(f"PHENOTYPE FILTER: {len(dangerous_cohort)} high-risk subjects isolated")
if len(dangerous_cohort) > 0:
    print(dangerous_cohort[['filename','type','notes']].head())
