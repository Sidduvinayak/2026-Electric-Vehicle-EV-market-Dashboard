import pandas as pd
import numpy as np

# Load the dataset
file_path = r"C:\Users\Gummadi\Downloads\ev_market_2026.csv"
df = pd.read_csv(file_path)

# ==========================
# 1. Display dataset info
# ==========================
print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:", df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

# ==========================
# 2. Clean column names
# ==========================
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
)

# ==========================
# 3. Remove duplicate rows
# ==========================
df.drop_duplicates(inplace=True)

# ==========================
# 4. Fill missing values
# ==========================

# Numeric columns → Median
numeric_cols = df.select_dtypes(include=["number"]).columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Text columns → Mode
text_cols = df.select_dtypes(include=["object"]).columns

for col in text_cols:
    if not df[col].mode().empty:
        df[col] = df[col].fillna(df[col].mode()[0])

# ==========================
# 5. Remove leading/trailing spaces in text columns
# ==========================
for col in text_cols:
    df[col] = df[col].astype(str).str.strip()

# ==========================
# 6. Remove fully empty rows
# ==========================
df.dropna(how="all", inplace=True)

# ==========================
# 7. Check remaining missing values
# ==========================
print("\nRemaining Missing Values:")
print(df.isnull().sum())

# ==========================
# 8. Save cleaned dataset
# ==========================
output_path = r"C:\Users\Gummadi\Downloads\ev_market_2026_cleaned.csv"
df.to_csv(output_path, index=False)

print("\nData cleaning completed successfully!")
print(f"Cleaned file saved to:\n{output_path}")