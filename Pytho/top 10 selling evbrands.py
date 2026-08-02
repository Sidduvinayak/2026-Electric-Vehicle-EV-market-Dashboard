import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned CSV file
file_path = r"C:\Users\Gummadi\Downloads\ev_market_2026_cleaned.csv"
df = pd.read_csv(file_path)

# Top 10 Selling EV Brands
top_brands = (
    df.groupby("brand")["annual_sales_units"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

# Plot
plt.figure(figsize=(10, 6))
plt.bar(top_brands.index, top_brands.values)
plt.title("Top 10 Selling EV Brands")
plt.xlabel("Brand")
plt.ylabel("Annual Sales Units")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.tight_layout()
plt.show()