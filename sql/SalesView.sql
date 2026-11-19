CREATE VIEW vw_pharma_sales AS
SELECT
    f.sales_id,
    d.date,
    d.year,
    d.month,
    d.weekday,
    f.hour,
    dr.drug_code,
    f.sales
FROM fact_sales_dw f
JOIN dim_date d
    ON f.date_id = d.date_id
JOIN dim_drug dr
    ON f.drug_id = dr.drug_id;

SELECT *
FROM vw_pharma_sales
LIMIT 20;

SELECT
    drug_code,
    SUM(sales) AS total_sales
FROM vw_pharma_sales
GROUP BY drug_code
ORDER BY total_sales DESC;