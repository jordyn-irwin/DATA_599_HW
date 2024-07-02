#Libraries

from pyspark.sql import SparkSession
import pandas as pd
import os

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

data = [['John', 19], ['Smith', 23], ['Sarah', 18]]

# Create the pandas DataFrame
pandas_df = pd.DataFrame(data, columns=['name', 'age'])

# Convert local data frame to a SparkDataFrame
df = spark.createDataFrame(pandas_df)

# Print its schema
df.printSchema()

# Create a DataFrame from a JSON file
path = os.path(os.environ("SPARK_HOME"), "examples/src/main/resources/people.json")
peopleDF = pd.read_json(path)
peopleDF.printSchema()

# Register this DataFrame as a table.
peopleDF.createOrReplaceTempView("people")

# SQL statements can be run by using the sql methods
teenagers = spark.sql("SELECT name FROM people WHERE age >= 13 AND age <= 19")

# Call collect to get a local data.frame
teenagersLocalDF = teenagers.collect()

# Print the teenagers in our dataset
print(teenagersLocalDF)

# Stop the SparkSession now
spark.stop()