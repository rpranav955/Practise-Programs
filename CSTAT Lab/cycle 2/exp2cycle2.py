import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("BankChurners.csv")

# Display first 5 rows
print(df.head())

# Dataset information
print(df.info())

# Check missing values
print(df.isnull().sum())

# Fill missing numerical values with median
for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].median())

# Fill missing categorical values with mode
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Verify missing values
print(df.isnull().sum())

print(df.head())

# Count customers in each category
print(df['churn'].value_counts())

# Plot pie chart
plt.figure(figsize=(7, 7))

df['churn'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90,
    labels=['Existing Customer', 'Attrited Customer']
)

plt.title("Customer Attrition Flag Ratio")
plt.ylabel("")
plt.show()


# Bar chart
plt.figure(figsize=(9, 5))

sns.countplot(data=df, x='country')

plt.title("Customers by Country")
plt.xlabel("Country")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45)
plt.show()

# Box plot for Customer Age
plt.figure(figsize=(7, 5))

sns.boxplot(y=df['age'])

plt.title("Box Plot of Customer Age")
plt.ylabel("Age")
plt.show()


# Box plot for Credit Limit
plt.figure(figsize=(7, 5))

sns.boxplot(y=df['credit_score'])

plt.title("Box Plot of Credit Score")
plt.ylabel("Credit Score")
plt.show()


# Box plot for Total Transaction Amount
plt.figure(figsize=(7, 5))

sns.boxplot(y=df['estimated_salary'])

plt.title("Box Plot of Estimated Salary")
plt.ylabel("Estimated Salary")
plt.show()

# Descriptive statistics for numerical columns
print(df.describe())

# Additional statistics
print("Mean:\n", df.mean(numeric_only=True))

print("\nMedian:\n", df.median(numeric_only=True))

print("\nStandard Deviation:\n", df.std(numeric_only=True))

# Select numerical columns
numeric_df = df.select_dtypes(include=np.number)

# Calculate correlation
correlation = numeric_df.corr()

# Plot heatmap
plt.figure(figsize=(12, 10))

sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm',
    fmt='.2f',
    linewidths=0.5
)

plt.title("Correlation Heatmap")
plt.show()


# Remove columns if they exist
df.drop(
    columns="tenure",
    errors='ignore',
    inplace=True
)

# Display remaining columns
print(df.columns)

print("\nUpdated Dataset:")
print(df.head())
