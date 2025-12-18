# ============================================================
# Azure Databricks — Bronze / Silver / Gold Pipeline
# ============================================================

# NOTE:
# This script is intended to be executed inside Azure Databricks
# where SparkSession (spark) is pre-initialized.

# ============================================================
# GLOBAL CONFIGURATION
# ============================================================

BASE_PATH = "/tmp/ai_data_engineering"

RAW_PATH    = "/databricks-datasets/learning-spark-v2/people/people-10m.parquet"
BRONZE_PATH = f"{BASE_PATH}/bronze/people"
SILVER_PATH = f"{BASE_PATH}/silver/people"
GOLD_PATH   = f"{BASE_PATH}/gold/people_metrics"

print("Path configuration:")
print("RAW   :", RAW_PATH)
print("BRONZE:", BRONZE_PATH)
print("SILVER:", SILVER_PATH)
print("GOLD  :", GOLD_PATH)

# ============================================================
# RAW INGESTION
# ============================================================

df_raw = spark.read.parquet(RAW_PATH)

df_raw.printSchema()
df_raw.show(5)

# ============================================================
# RAW → BRONZE
# ============================================================

df_raw.write \
    .mode("overwrite") \
    .format("delta") \
    .save(BRONZE_PATH)

print("✅ Bronze saved as Delta:", BRONZE_PATH)

# ============================================================
# VALIDATE BRONZE
# ============================================================

df_bronze = spark.read.format("delta").load(BRONZE_PATH)

df_bronze.count()
df_bronze.show(5)

# ============================================================
# BRONZE → SILVER (CLEANING + PII REMOVAL)
# ============================================================

from pyspark.sql.functions import col, lower, trim

df_silver = (
    df_bronze
    .dropna(subset=["id", "firstName", "lastName"])
    .withColumn("firstName", trim(lower(col("firstName"))))
    .withColumn("lastName", trim(lower(col("lastName"))))
    .withColumn("gender", trim(lower(col("gender"))))
    .drop("ssn")  # PII removal
)

df_silver.printSchema()
df_silver.show(5)

# ============================================================
# SAVE SILVER
# ============================================================

df_silver.write \
    .mode("overwrite") \
    .format("delta") \
    .save(SILVER_PATH)

print("✅ Silver saved as Delta:", SILVER_PATH)

# ============================================================
# VALIDATE SILVER
# ============================================================

df_silver_check = spark.read.format("delta").load(SILVER_PATH)

df_silver_check.count()
df_silver_check.show(5)

# ============================================================
# SILVER → GOLD (BUSINESS METRICS)
# ============================================================

from pyspark.sql import functions as F

df_gold = (
    df_silver
    .groupBy("gender")
    .agg(
        F.count("*").alias("total_people"),
        F.avg("salary").alias("avg_salary"),
        F.min("salary").alias("min_salary"),
        F.max("salary").alias("max_salary")
    )
)

df_gold.printSchema()
df_gold.show()

# ============================================================
# SAVE GOLD
# ============================================================

df_gold.write \
    .mode("overwrite") \
    .format("delta") \
    .save(GOLD_PATH)

print("✅ Gold saved as Delta:", GOLD_PATH)

# ============================================================
# REGISTER DELTA TABLES
# ============================================================

spark.sql("CREATE DATABASE IF NOT EXISTS ai_data_engineering")

spark.sql(f"""
CREATE TABLE IF NOT EXISTS ai_data_engineering.bronze_people
USING DELTA
LOCATION '{BRONZE_PATH}'
""")

spark.sql(f"""
CREATE TABLE IF NOT EXISTS ai_data_engineering.silver_people
USING DELTA
LOCATION '{SILVER_PATH}'
""")

spark.sql(f"""
CREATE TABLE IF NOT EXISTS ai_data_engineering.gold_people_metrics
USING DELTA
LOCATION '{GOLD_PATH}'
""")

print("✅ Delta tables registered successfully")

spark.sql("SHOW TABLES IN ai_data_engineering").show()