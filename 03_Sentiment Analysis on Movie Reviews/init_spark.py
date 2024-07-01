from pyspark.sql import SparkSession
from pyspark.sql.functions import lower, regexp_replace


def init_spark():
    spark = SparkSession \
        .builder \
        .appName("Python Spark Movie Reviws Analysis") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

    path = "./docs/movie_reviews.csv"
    df = spark.read.option("delimiter", ",").option("header", True).option("quote", "\"").option("escape", "\"").csv(path)
    df = df.withColumn('review', lower(df['review']))
    df = df.withColumn('review', regexp_replace(df['review'], r"""[!\"#$%&'()*+,\-.\/:;<=>?@\[\\\]^_`{|}~]"""," "))
    df.show()

    # Split data
    train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)

    train_csv_path = "train.csv"
    test_csv_path = "test.csv"

    train_df = train_df.repartition(10)
    test_df = test_df.repartition(10)
    train_df.coalesce(1).write.option("header", "true").mode('overwrite').csv(train_csv_path)
    test_df.coalesce(1).write.option("header", "true").mode('overwrite').csv(test_csv_path)

    spark.stop()