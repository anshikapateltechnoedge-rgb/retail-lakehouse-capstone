# Silver and gold layers of the retail capstone (Lakeflow Declarative Pipelines)
from pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.table(comment="Clean orders with revenue")
@dp.expect_or_drop("valid_quantity", "Quantity > 0")
@dp.expect_or_drop("valid_city", "City IS NOT NULL")
@dp.expect("valid_price", "Price > 0")
def silver_orders(): return spark.readStream.table("workspace.capstone.bronze_orders").select("OrderID", "OrderDate", "City", "Product", "Quantity", "Price").withColumn("Revenue", F.col("Quantity") * F.col("Price"))

@dp.materialized_view(comment="Revenue and orders by city")
def gold_revenue_by_city(): return spark.read.table("silver_orders").groupBy("City").agg(F.sum("Revenue").alias("TotalRevenue"), F.count("*").alias("Orders"))
