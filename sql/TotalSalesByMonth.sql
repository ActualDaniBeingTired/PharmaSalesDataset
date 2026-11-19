SELECT
    d.year,
    d.month,
    SUM(f.sales) AS total_sales
FROM fact_sales_dw f
JOIN dim_date d
    ON f.date_id = d.date_id
GROUP BY
    d.year,
    d.month
ORDER BY
    d.year,
    d.month;