from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, regexp_replace, count, round, sum

spark = SparkSession \
    .builder \
    .appName("Python Spark Movie Reviws Analysis") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

path = "./movie_reviews.csv"
df = spark.read.option("delimiter", ",").option("header", True).option("quote", "\"").option("escape", "\"").csv(path)
#df['review'] = df['review'].str.lower()
df = df.withColumn('review', lower(df['review']))
df = df.withColumn('review', regexp_replace(df['review'], r"""[!\"#$%&'()*+,\-.\/:;<=>?@\[\\\]^_`{|}~]"""," "))
df.show()

# Split data
train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)

train_csv_path = "train.csv"
test_csv_path = "test.csv"
targetvar = "sentiment"

trainrows = train_df.count()
train_df.groupBy(targetvar).agg(count(targetvar).alias('Count')).withColumn("distribution", round((col('Count') / trainrows * 100))).orderBy(targetvar).show()

testrows = test_df.count()
test_df.groupBy(targetvar).agg(count(targetvar).alias('Count')).withColumn("distribution", round((col('Count') / testrows * 100))).orderBy(targetvar).show()
print(train_df.count())
print(test_df.count())

train_df = train_df.repartition(10)
test_df = test_df.repartition(10)
train_df.coalesce(1).write.option("header", "true").mode('overwrite').csv(train_csv_path)
test_df.coalesce(1).write.option("header", "true").mode('overwrite').csv(test_csv_path)

spark.stop()