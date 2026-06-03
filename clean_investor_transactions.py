import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# Convert date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

# Keep only positive amounts
df = df[df["amount_inr"] > 0]

# Remove duplicates
df = df.drop_duplicates()

# Check KYC values
print("\nKYC Status Values:")
print(df["kyc_status"].unique())

print("\nCleaned Shape:", df.shape)

df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

print("Saved Successfully")