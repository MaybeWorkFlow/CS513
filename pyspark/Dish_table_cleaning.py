# PySpark for Data Cleaning project

def singleSpace(row,colName):
    data = row.asDict()
    text = data[colName]
    spaceCount = 0;
    Words = []
    word = ''

    for char in text:
        if char != ' ':
            word += char
        elif word == '' and char == ' ':
            continue
        else:
            Words.append(word)
            word = ''

    if len(Words) > 0:
    data[colName] = ' '.join(Words)

    return Row(**data)


# Load data from CSV file. Inferschema will automatically detect datatypes as integers, decimals and strings
df = spark.read.format("csv").option("header", "true")
			     .option("inferSchema", "true")
			     .load("Dish.csv")

# Convert data to lower case
df_lower = df.toDF(*[c.lower() for c in df.columns])

# Record data into a CSV after converting case for provenance
df.write.csv('Dish_lower.csv')

# Cleanup trailing whitespaces and
# convert all multiple white spaces to single white space
df_lower = df.toDF(*[c.lower() for c in df.columns])
df = df.withColumn('name',ltrim(df['name'])
df = df.withColumn('name',rtrim(df['name']))
df = df.rdd.map(lambda row: singleSpace(row,;'name')).toDF()

# Record data into a CSV after cleaning up white spaces for provenance
df.write.csv('Dish_whitespace_cleanup.csv')

# Remove description column because it has no values
df.drop('description')

# Record data into a CSV after removing a column for provenance
df.write.csv('Dish_description_deleted.csv')

# Cluster rows based on name column to find dupicate entries
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.ml.clustering import KMeans

features = ('name')
assembler = VectorAssembler(inputCols=features,outputCol="features")

dataset=assembler.transform(df)
dataset.select("features").show(truncate=False)
kmeans = KMeans().setK(df.count()/4).setSeed(1)
model = kmeans.fit(dataset)
predictions = model.transform(dataset)

df1 = predictions.toDF()
df1.orderBy('prediction', ascending=False)

# Record data into a CSV after creating clusters
df.write.csv('Dish_clusters.csv')
