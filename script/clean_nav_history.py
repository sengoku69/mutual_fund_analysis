import pandas as pd


df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)


df["date"] = pd.to_datetime(df["date"])


df = df.sort_values(
    by=["amfi_code", "date"]
)


df = df.drop_duplicates()


df["nav"] = (
    df.groupby("amfi_code")["nav"]
      .ffill()
)


df = df[df["nav"] > 0]

print("Cleaned Shape:", df.shape)


df.to_csv(
    "data/processed/nav_history_cleaned.csv",
    index=False
)

print("Saved Successfully")