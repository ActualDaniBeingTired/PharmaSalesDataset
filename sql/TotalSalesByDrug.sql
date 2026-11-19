SELECT
    dr.drug_code,
    SUM(f.sales) AS total_sales
FROM fact_sales_dw f
JOIN dim_drug dr
    ON f.drug_id = dr.drug_id
GROUP BY dr.drug_code
ORDER BY total_sales DESC;