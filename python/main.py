import os
from datetime import datetime
from typing import Tuple, List

import pyspark

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import LongType, StringType, StructField, StructType, IntegerType

from text_stats import text_stats


PROJECT_ROOT_PATH = os.path.realpath('..')
DATASET_PATH = os.path.join(PROJECT_ROOT_PATH, 'data', 'sample_data.json')
SCALA_ARTIFACTS_PATH = os.path.join(PROJECT_ROOT_PATH, 'scala', 'target', 'scala-2.12', 'spark-udf-assembly-0.1.0.jar')

spark = SparkSession.builder \
                    .config('spark.driver.memory', '8g') \
                    .config('spark.driver.extraClassPath', SCALA_ARTIFACTS_PATH) \
                    .getOrCreate()

data_schema = StructType([
    StructField('text', StringType(), nullable=False),
    StructField('timestamp', LongType(), nullable=False),
])

udf_schema = StructType([
    StructField('word_count', IntegerType(), nullable=False),
    StructField('char_count', IntegerType(), nullable=False)
])

text_stats_python_udf = F.udf(text_stats.get_text_stats, udf_schema)

spark.udf.registerJavaFunction('textStats', 'com.github.mvinesn.TextStatsUDF', udf_schema)

sample_data = [
    {'text': 'Hello World', 'timestamp': 1657776567},
    {'text': 'Enjoy your day', 'timestamp': 1657776567},
    {'text': 'I am surrounded by Kangaroos', 'timestamp': 1657776567},
    {'text': 'Cacti have water but are not yummy', 'timestamp': 1657776567},
]

df = spark.createDataFrame(sample_data)

df_scala_udf = df.withColumn('extracted', F.expr('textStats(text)')) \
                 .select(F.col('text'), F.col('timestamp'), F.col('extracted.*')) \
                 .collect()

df_python_udf = df.withColumn('extracted', text_stats_python_udf(F.col('text'))) \
                  .select(F.col('text'), F.col('timestamp'), F.col('extracted.*')) \
                  .collect()

