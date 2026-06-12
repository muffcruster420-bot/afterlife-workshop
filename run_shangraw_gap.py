import pandas as pd

# Phenotype filter for Shangraw Gap stress-test
# Jesse Shangraw — Kingston, ON — June 12 2026
df = pd.read_csv('subjects_metadata.csv')

dangerous_mask = (
    df['icd10'].isin(['G40.9', 'G93.4']) |
    (df['ketamine_last_60min'] == 1)
)
dangerous_cohort = df[dangerous_mask]

print(f"PHENOTYPE FILTER: {len(dangerous_cohort)} high-risk subjects isolated")
