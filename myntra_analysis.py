
import pandas as pd

# Myntra dataset load karna
df = pd.read_csv("train.csv")

# Pehli 5 rows dekhna
print("MYNTRA DATASET")
print(df.head())

# Dataset ki information
print("\nDATASET INFORMATION")
print(df.info())

# Rows aur columns ki sankhya
print("\nROWS AND COLUMNS")
print(df.shape)

# Column names
print("\nCOLUMN NAMES")
print(df.columns.tolist())


# Missing values check karna
print("\nMISSING VALUES")
print(df.isnull().sum())

# Duplicate rows check karna
print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

# Myntra ke brands dekhna
print("\nTOP 10 BRANDS")
print(df["brand"].value_counts().head(10))

# Product prices ka summary
print("\nPRICE SUMMARY")
print(df["variant_price"].describe())


import matplotlib.pyplot as plt

# Top 10 brands ka graph
top_brands = df["brand"].value_counts().head(10)

plt.figure(figsize=(10, 5))
top_brands.plot(kind="bar")
plt.title("Top 10 Myntra Brands")
plt.xlabel("Brand")
plt.ylabel("Number of Products")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Product price ka graph
prices = pd.to_numeric(df["variant_price"], errors="coerce").dropna()

plt.figure(figsize=(8, 5))
prices.plot(kind="hist", bins=20)
plt.title("Myntra Product Price Distribution")
plt.xlabel("Price")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.show()

# IMPORTANT FINDINGS

print("\n===== MYNTRA DATA ANALYSIS FINDINGS =====")

# Total products
print("Total Products:", len(df))

# Top 5 brands
print("\nTop 5 Brands:")
print(df["brand"].value_counts().head(5))

# Average product price
prices = pd.to_numeric(df["variant_price"], errors="coerce").dropna()
print("\nAverage Product Price:", round(prices.mean(), 2))

# Lowest and highest price
print("Lowest Product Price:", prices.min())
print("Highest Product Price:", prices.max())

# FINAL PROJECT SUMMARY

print("\n===== FINAL PROJECT SUMMARY =====")
print("1. Myntra product data ka analysis kiya gaya.")
print("2. Top 10 brands ka graph banaya gaya.")
print("3. Product prices ka distribution graph banaya gaya.")
print("4. Average, minimum aur maximum prices calculate kiye gaye.")
print("5. Data analysis se product brands aur prices ko samajhne mein madad mili.")
