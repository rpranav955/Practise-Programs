import pandas as pd

# Read the CSV file
df = pd.read_csv("murder.csv")

# Calculate statistics for Population
print("Population Statistics")
print("Mean:", df["Population"].mean())
print("Median:", df["Population"].median())
print("Variance:", df["Population"].var(ddof=0))

# Calculate statistics for Murder Rate
print("\nMurder Rate Statistics")
print("Mean:", df["Murder.Rate"].mean())
print("Median:", df["Murder.Rate"].median())
print("Variance:", df["Murder.Rate"].var(ddof=0))
