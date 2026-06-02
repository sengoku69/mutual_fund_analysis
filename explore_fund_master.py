import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("\nFund Houses:")
print(df["fund_house"].unique())

print("\nCategories:")
print(df["category"].unique())

print("\nSub Categories:")
print(df["sub_category"].unique())

print("\nTotal Fund Houses:",
      df["fund_house"].nunique())

print("\nTotal Categories:",
      df["category"].nunique())

print("\nTotal Sub Categories:",
      df["sub_category"].nunique())