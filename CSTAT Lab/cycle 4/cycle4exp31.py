import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("lois_continuous.csv", header=1)
df.columns = df.columns.str.strip()

swale_data = df[
    df["SITE_NAME"].astype(str).str.strip() == "Swale at Catterick Bridge"
].copy()

print("Number of records:", len(swale_data))

temp_col = "0476 (Cel)"
oxy_col = "0474 (% satn)"

# Make sure they're numeric (in case of stray text)
swale_data[temp_col] = pd.to_numeric(swale_data[temp_col], errors="coerce")
swale_data[oxy_col] = pd.to_numeric(swale_data[oxy_col], errors="coerce")

mean_temperature = swale_data[temp_col].mean()
median_oxygen = swale_data[oxy_col].median()

print("Mean temperature:", round(mean_temperature, 2), "°C")
print("Median dissolved oxygen:", round(median_oxygen, 2), "% saturation")

plt.hist(swale_data[temp_col].dropna(), bins=15, edgecolor="black")
plt.title("Water Temperature - Swale at Catterick Bridge")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.show()
