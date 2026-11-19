CREATE TABLE IF NOT EXISTS dim_drug (
    drug_id SERIAL PRIMARY KEY,
    drug_code VARCHAR(10) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS dim_date (
    date_id SERIAL PRIMARY KEY,
    date DATE UNIQUE NOT NULL,
    year INT NOT NULL,
    month INT NOT NULL,
    weekday VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS fact_sales_dw (
    sales_id SERIAL PRIMARY KEY,
    date_id INT NOT NULL,
    drug_id INT NOT NULL,
    hour INT NOT NULL,
    sales NUMERIC(10, 2) NOT NULL,

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id),

    FOREIGN KEY (drug_id)
        REFERENCES dim_drug(drug_id)
);