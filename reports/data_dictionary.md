# Data Dictionary

## 01_fund_master.csv

| Column        | Type | Description |
| amfi_code     | Integer | Unique AMFI Scheme Code |
| fund_house    | Text | Mutual Fund House |
| scheme_name   | Text | Scheme Name |
| category      | Text | Fund Category |
| sub_category  | Text | Fund Sub Category |

---

## 02_nav_history.csv

| Column         | Type | Description |
| amfi_code      | Integer | Scheme Code |
| date           | Date  | NAV Date |
| nav            | Float | Net Asset Value |

## 08_investor_transactions.csv

| Column                  | Type | Description |
| investor_id             | Text | Investor Identifier |
| transaction_date        | Date | Transaction Date |
| transaction_type        | Text | SIP/Lumpsum/Redemption |
| amount_inr              | Float | Transaction Amount |
| kyc_status              | Text | Investor KYC Status |