import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
file_path = r"C:\Users\Gummadi\Downloads\ev_market_2026_cleaned.csv"
df = pd.read_csv(file_path)

# Display column names
print(df.columns.tolist())