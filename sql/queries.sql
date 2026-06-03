-- 1. Top 5 Funds by AUM

SELECT
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV per Fund

SELECT
    amfi_code,
    AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;


-- 3. Highest 1-Year Return

SELECT
    amfi_code,
    return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;


-- 4. Funds with Expense Ratio < 1%

SELECT
    amfi_code,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;


-- 5. Total Transactions by State

SELECT
    state,
    COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY state
ORDER BY transaction_count DESC;


-- 6. Total Investment Amount by State

SELECT
    state,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;


-- 7. Transactions by Type

SELECT
    transaction_type,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;


-- 8. Verified vs Pending KYC

SELECT
    kyc_status,
    COUNT(*) AS total_investors
FROM fact_transactions
GROUP BY kyc_status;


-- 9. Average Expense Ratio

SELECT
    AVG(expense_ratio_pct) AS avg_expense_ratio
FROM fact_performance;


-- 10. Highest AUM Fund

SELECT
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 1;