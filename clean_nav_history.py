import pandas as pd

# Load data
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort
df = df.sort_values(
    by=["amfi_code", "date"]
)

# Remove duplicates
df = df.drop_duplicates()

# Forward fill NAV within each fund
df["nav"] = (
    df.groupby("amfi_code")["nav"]
      .ffill()
)

# Keep only positive NAV values
df = df[df["nav"] > 0]

print("Cleaned Shape:", df.shape)

# Save
df.to_csv(
    "data/processed/nav_history_cleaned.csv",
    index=False
)

print("Saved Successfully")