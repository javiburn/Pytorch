import spark
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark Movie Reviws Analysis") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

path = "./movie_reviews.csv"
df = spark.read.option("delimiter", ",").option("header", True).option("quote", "\"").option("escape", "\"").csv(path)
df.show()