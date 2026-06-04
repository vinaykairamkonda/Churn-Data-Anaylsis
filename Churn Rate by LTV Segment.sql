SELECT
    ltv_segment,
    ROUND(
        100.0 * SUM(CASE WHEN churn='Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_rate
FROM telco_customers
GROUP BY ltv_segment;