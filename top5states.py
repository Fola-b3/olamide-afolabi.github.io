import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("cleaned_crime_data.csv")

latest_year = df["Year"].max()

df_latest = df[df["Year"] == latest_year]



top5_safest = (
    df_latest
    .sort_values("Data.Rates.Violent.All", ascending=True)
    .head(5)
)

total_violent = df_latest["Data.Totals.Violent.All"].sum()
total_pop = df_latest["Data.Population"].sum()
us_avg_violent_rate = (total_violent / total_pop) * 100000

\

states = top5_safest["State"]
rates = top5_safest["Data.Rates.Violent.All"]

colors = ["tab:green"] + ["tab:blue"] * (len(states) - 1)

plt.figure(figsize=(10, 5))

plt.barh(states, rates, color=colors)

plt.axvline(us_avg_violent_rate, linestyle="--", color="black")

plt.title(
    f"These are the top 5 states with the lowest violent crime rates per 100,000 people. "
    f"The U.S. average is {us_avg_violent_rate:.1f}.",
    loc="center",
    fontsize=15,
    weight="bold"
)



plt.xlabel("Violent crime rate per 100,000 people")
plt.ylabel("State") 

for i, rate in enumerate(rates):
    plt.text(
        rate + 5,      # slightly right of the bar
        i,
        f"{rate:.1f}",
        va="center",
        fontsize=9
    )

plt.text(
    us_avg_violent_rate + 3,
    -0.4,
    f"U.S. Avg ({us_avg_violent_rate:.1f})",
    fontsize=9,
    va="center"
)

plt.tight_layout()
plt.show()
