# Retail Lakehouse on Databricks

End-to-end medallion pipeline for retail orders, built on Databricks with Unity Catalog.

## Architecture
- **Bronze:** Auto Loader ingests CSV files from a Unity Catalog volume (`bronze_orders`)
- **Silver:** declarative pipeline with data quality expectations (`silver_orders`)
- **Gold:** materialized views for revenue by city, product and month
- **Orchestration:** Lakeflow Job `capstone_daily`, deployed as a bundle
- **Governance:** grants and a column mask on PII

## Results
- 7 raw orders in, 2 invalid rows dropped, 5 clean orders
- Gold totals validated against silver: 268,000 = 268,000

## Skills
PySpark, Spark SQL, Delta Lake, Auto Loader, Lakeflow Declarative Pipelines, Lakeflow Jobs, Unity Catalog, Bundles
