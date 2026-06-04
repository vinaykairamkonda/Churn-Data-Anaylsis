SELECT
    ltv_segment,
    SUM(monthlycharges) AS revenue
FROM telco_customers
GROUP BY ltv_segment;