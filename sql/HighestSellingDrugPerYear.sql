WITH yearly_sales AS (
    SELECT
        d.year,
        dr.drug_code,
        SUM(f.sales) AS total_sales
    FROM fact_sales_dw f
    JOIN dim_date d
        ON f.date_id = d.date_id
    JOIN dim_drug dr
        ON f.drug_id = dr.drug_id
    GROUP BY
        d.year,
        dr.drug_code
),

ranked_sales AS (
    SELECT
        year,
        drug_code,
        total_sales,
        RANK() OVER (
            PARTITION BY year
            ORDER BY total_sales DESC
        ) AS sales_rank
    FROM yearly_sales
)

SELECT
    year,
    drug_code,
    total_sales
FROM ranked_sales
WHERE sales_rank = 1
ORDER BY year;