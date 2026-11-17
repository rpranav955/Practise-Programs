import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("lois_continuous.csv", header=1)


filtered_df = df[df["SITE_NAME"] == "Swale at Catterick Bridge"]


mean_temp = filtered_df["0476 (Cel)"].mean()
median_oxygen = filtered_df["0474 (% satn)"].median()

print("Mean Temperature:", mean_temp)
print("Median Dissolved Oxygen:", median_oxygen)


plt.hist(filtered_df["0476 (Cel)"], bins=20, edgecolor="black")

plt.title("River Water Temperature Distribution")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")

plt.show()
