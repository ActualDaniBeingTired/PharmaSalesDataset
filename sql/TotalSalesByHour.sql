SELECT
    hour,
    SUM(sales) AS total_sales
FROM fact_sales_dw
GROUP BY hour
ORDER BY total_sales DESC;