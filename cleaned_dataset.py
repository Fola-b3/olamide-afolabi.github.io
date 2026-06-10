import pandas as pd


df = pd.read_csv("state_crime (2).csv")

cols_needed = [
    "State",
    "Year",
    "Data.Population",
    "Data.Rates.Violent.All",
    "Data.Totals.Violent.All"
]
df = df[cols_needed].copy()

df = df[(df["Year"] >= 2000) & (df["Year"] <= 2019)]

df_states = df[df["State"] != "United States"].copy()

numeric_cols = ["Data.Population", "Data.Rates.Violent.All", "Data.Totals.Violent.All"]
for col in numeric_cols:
    df_states[col] = pd.to_numeric(df_states[col], errors="coerce")

df_states = df_states.dropna(subset=numeric_cols)

df_states.to_csv("cleaned_crime_data.csv", index=False)


