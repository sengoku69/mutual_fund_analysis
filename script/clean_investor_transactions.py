import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)


df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)


df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)


df = df[df["amount_inr"] > 0]


df = df.drop_duplicates()


print("\nKYC Status Values:")
print(df["kyc_status"].unique())

print("\nCleaned Shape:", df.shape)

df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

print("Saved Successfully")