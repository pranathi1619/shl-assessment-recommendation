import pandas as pd

df = pd.read_excel("Gen_AI Dataset.xlsx")

# Rename columns to match pipeline
df = df.rename(columns={
    df.columns[0]: "assessment_name",
    df.columns[1]: "description"
})

df["job_role"] = "General"
df["skills"] = "General"

df.to_csv("data/assessments.csv", index=False)

print("Converted Excel to assessments.csv")
