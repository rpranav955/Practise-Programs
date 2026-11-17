
import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("sales.csv")

# Convert date column
df["Sale_Date"] = pd.to_datetime(df["Sale_Date"])

# Calculate profit
df["Profit"] = df["Sales_Amount"] - (
    df["Unit_Cost"] * df["Quantity_Sold"]
)

# Extract month
df["Month"] = df["Sale_Date"].dt.month

# Monthly calculations
monthly_sales = df.groupby("Month")["Sales_Amount"].sum()
monthly_profit = df.groupby("Month")["Profit"].sum()

# Monthly sales by product category
monthly_category = df.pivot_table(
    index="Month",
    columns="Product_Category",
    values="Sales_Amount",
    aggfunc="sum"
)


# (a) Total Profit Line Plot
plt.plot(monthly_profit.index, monthly_profit.values)

plt.title("Monthly Total Profit")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.grid()

plt.show()


# (b) Styled Line Plot
plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    color="red",
    marker="o",
    linestyle="--",
    linewidth=2,
    markersize=6
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.grid()

plt.show()


# (c) Multi-Line Plot
for category in monthly_category.columns:
    plt.plot(
        monthly_category.index,
        monthly_category[category],
        marker="o",
        label=category
    )

plt.title("Monthly Sales by Product Category")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.legend()
plt.grid()

plt.show()


# (d) Scatter Plot
plt.scatter(
    df["Quantity_Sold"],
    df["Sales_Amount"],
    color="green"
)

plt.title("Quantity Sold vs Sales Amount")
plt.xlabel("Quantity Sold")
plt.ylabel("Sales Amount")

plt.show()


# (e) Bar Chart
category_sales = df.groupby("Product_Category")["Sales_Amount"].sum()

plt.bar(category_sales.index, category_sales.values)

plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")

# (f) Save Figure
plt.savefig("sales_bar_chart.png")

plt.show()



# (g) Histogram
plt.hist(df["Sales_Amount"], bins=20, edgecolor="black")

plt.title("Distribution of Sales Amount")
plt.xlabel("Sales Amount")
plt.ylabel("Frequency")

plt.show()


# (h) Pie Chart
plt.pie(
    category_sales.values,
    labels=category_sales.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sales Distribution by Product Category")

plt.show()


# (i) Subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Line plot
axes[0, 0].plot(monthly_sales.index, monthly_sales.values)
axes[0, 0].set_title("Monthly Sales")

# Bar chart
axes[0, 1].bar(category_sales.index, category_sales.values)
axes[0, 1].set_title("Category Sales")

# Histogram
axes[1, 0].hist(df["Sales_Amount"], bins=15)
axes[1, 0].set_title("Sales Distribution")

# Scatter plot
axes[1, 1].scatter(df["Quantity_Sold"], df["Sales_Amount"])
axes[1, 1].set_title("Quantity vs Sales")

plt.show()


# (j) Stack Plot
plt.stackplot(
    monthly_category.index,
    *[monthly_category[col] for col in monthly_category.columns],
    labels=monthly_category.columns
)

plt.title("Monthly Sales by Product Category")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.legend()

plt.show()
