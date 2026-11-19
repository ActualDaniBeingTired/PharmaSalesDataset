SELECT
    d.weekday,
    SUM(f.sales) AS total_sales
FROM fact_sales_dw f
JOIN dim_date d
    ON f.date_id = d.date_id
GROUP BY d.weekday
ORDER BY total_sales DESC;