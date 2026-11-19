SELECT
    d.year,
    d.month,
    dr.drug_code,
    SUM(f.sales) AS total_sales
FROM fact_sales_dw f
JOIN dim_date d
    ON f.date_id = d.date_id
JOIN dim_drug dr
    ON f.drug_id = dr.drug_id
GROUP BY
    d.year,
    d.month,
    dr.drug_code
ORDER BY
    d.year,
    d.month,
    total_sales DESC;