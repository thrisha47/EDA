import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    "Date": [
        "2025-01-01", "2025-01-05", "2025-01-10",
        "2025-02-01", "2025-02-08", "2025-02-15",
        "2025-03-01", "2025-03-10", "2025-03-18",
        "2025-03-25"
    ],
    "Product": [
        "Laptop", "Phone", "Shoes", "Watch", "Bag",
        "Laptop", "Phone", "Shoes", "Watch", "Bag"
    ],
    "Category": [
        "Electronics", "Electronics", "Fashion",
        "Accessories", "Fashion",
        "Electronics", "Electronics", "Fashion",
        "Accessories", "Fashion"
    ],
    "Sales": [10, 15, 20, 12, 18, 14, 17, 25, 11, 22],
    "Revenue": [50000, 45000, 20000, 18000, 15000,
                70000, 52000, 25000, 19000, 22000],
    "Customer_ID": [101, 102, 103, 104, 105,
                    106, 107, 108, 109, 110]
}
df = pd.DataFrame(data)
print("\n===== FIRST 5 ROWS =====")
print(df.head())
print("\n===== DATASET INFO =====")
print(df.info())
print("\n===== DESCRIPTIVE STATISTICS =====")
print(df.describe())
numerical_cols = ["Sales", "Revenue"]
for col in numerical_cols:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.show()
plt.figure(figsize=(8,5))
sns.heatmap(df[["Sales", "Revenue"]].corr(),
            annot=True,
            cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
top_products = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)
print("\nTop Products by Revenue:")
print(top_products)
plt.figure(figsize=(8,5))
top_products.plot(kind="bar")
plt.title("Top Products by Revenue")
plt.ylabel("Revenue")
plt.show()
category_sales = df.groupby("Category")["Sales"].sum()
plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Sales")
plt.show()
df["Date"] = pd.to_datetime(df["Date"])
monthly_sales = (
    df.groupby(df["Date"].dt.to_period("M"))["Sales"]
    .sum()
)
monthly_sales.index = monthly_sales.index.astype(str)
plt.figure(figsize=(10,5))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
print("\n===== KPI SUMMARY =====")
print("Total Sales:", df["Sales"].sum())
print("Total Revenue:", df["Revenue"].sum())
print("Total Customers:", df["Customer_ID"].nunique())
print("\nEDA & Business Intelligence Analysis Completed!")