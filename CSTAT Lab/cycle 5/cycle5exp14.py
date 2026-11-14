import pandas as pd
import matplotlib.pyplot as plt

# ---- Load data ----
df = pd.read_csv("sales.csv")
df["Sale_Date"] = pd.to_datetime(df["Sale_Date"])
df["Profit"] = (df["Unit_Price"] - df["Unit_Cost"]) * df["Quantity_Sold"]
df["Month"] = df["Sale_Date"].dt.month

monthly_profit = df.groupby("Month")["Profit"].sum()
months = monthly_profit.index.to_numpy()
profit_vals = monthly_profit.to_numpy()

cat_sales = df.groupby("Product_Category")["Sales_Amount"].sum()
cats = cat_sales.index.to_numpy()
cat_vals = cat_sales.to_numpy()

region_profit = df.pivot_table(index="Month", columns="Region",
                               values="Profit", aggfunc="sum").fillna(0)
rp_months = region_profit.index.to_numpy()

# (a) Total profit line plot
plt.figure(figsize=(8, 4))
plt.plot(months, profit_vals)
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

# (b) Styled line plot
plt.figure(figsize=(8, 4))
plt.plot(months, profit_vals, color="green", linestyle="--",
         marker="o", linewidth=2, markersize=7, label="Profit")
plt.title("Total Profit per Month (Styled)")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.grid(True)
plt.legend()
plt.show()

# (c) Multi line plot (profit per region)
plt.figure(figsize=(8, 4))
for region in region_profit.columns:
    plt.plot(rp_months, region_profit[region].to_numpy(), marker="o", label=region)
plt.title("Monthly Profit by Region")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.legend()
plt.show()

# (d) Scatter plot
plt.figure(figsize=(8, 4))
plt.scatter(df["Quantity_Sold"].to_numpy(), df["Sales_Amount"].to_numpy(),
            c="purple", alpha=0.6)
plt.title("Quantity Sold vs Sales Amount")
plt.xlabel("Quantity Sold")
plt.ylabel("Sales Amount")
plt.show()

# (e) Bar chart
plt.figure(figsize=(8, 4))
plt.bar(cats, cat_vals, color="skyblue")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales Amount")
plt.show()

# (f) Bar chart + save figure
plt.figure(figsize=(8, 4))
plt.bar(cats, cat_vals, color="orange")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales Amount")
plt.savefig("category_sales_bar.png", dpi=300, bbox_inches="tight")
plt.show()

# (g) Histogram
plt.figure(figsize=(8, 4))
plt.hist(df["Sales_Amount"].to_numpy(), bins=10, color="teal", edgecolor="black")
plt.title("Distribution of Sales Amount")
plt.xlabel("Sales Amount")
plt.ylabel("Frequency")
plt.show()

# (h) Pie chart
region_sales = df.groupby("Region")["Sales_Amount"].sum()
plt.figure(figsize=(6, 6))
plt.pie(region_sales.to_numpy(), labels=list(region_sales.index),
        autopct="%1.1f%%", startangle=90)
plt.title("Sales Share by Region")
plt.show()

# (i) Subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
axs[0, 0].plot(months, profit_vals, marker="o")
axs[0, 0].set_title("Monthly Profit")
axs[0, 1].bar(cats, cat_vals, color="skyblue")
axs[0, 1].set_title("Sales by Category")
axs[1, 0].hist(df["Sales_Amount"].to_numpy(), bins=10, color="teal", edgecolor="black")
axs[1, 0].set_title("Sales Amount Histogram")
axs[1, 1].scatter(df["Quantity_Sold"].to_numpy(), df["Sales_Amount"].to_numpy(), alpha=0.6)
axs[1, 1].set_title("Quantity vs Sales")
plt.tight_layout()
plt.show()

# (j) Stack plot
plt.figure(figsize=(8, 4))
plt.stackplot(rp_months,
              [region_profit[r].to_numpy() for r in region_profit.columns],
              labels=list(region_profit.columns))
plt.title("Stacked Profit by Region")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.legend(loc="upper left")
plt.show()
