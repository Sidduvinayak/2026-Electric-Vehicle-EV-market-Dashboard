import pandas as pd

df = pd.read_csv(r"C:\Users\Gummadi\Downloads\ev_market_2026_cleaned.csv")
print("Total Sales", df['total_sales'].sum())
print(df.groupby('country')['total_sales'].sum())
print(df.groupby('country')['total_sales'].sum().sort_values(ascending=False).head(10))