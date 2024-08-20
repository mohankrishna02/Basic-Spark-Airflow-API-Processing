import requests
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark import *
from pyspark.sql.types import *

conf = SparkConf().setMaster("local[*]").setAppName("apiprocessing")
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")

spark = SparkSession.builder.getOrCreate()

url = "https://randomuser.me/api/0.8/?results=20"
response = requests.get(url)
urldata = response.text

rdd = sc.parallelize([urldata])
df = spark.read.json(rdd)

df.show()
df.printSchema()

explodedf = df.withColumn("results",explode("results"))
explodedf.printSchema()

finaldf = explodedf.select("nationality",
            "seed",
            "version",
            "results.user.cell",
            "results.user.dob",
            "results.user.email",
            "results.user.gender",
            "results.user.location.city",
            "results.user.location.state",
            "results.user.location.street",
            "results.user.location.zip",
            "results.user.md5",
            "results.user.name.first",
            "results.user.name.last",
            "results.user.name.title",
            "results.user.password",
            "results.user.phone",
            "results.user.picture.large",
            "results.user.picture.medium",
            "results.user.picture.thumbnail",
            "results.user.registered",
            "results.user.salt",
            "results.user.sha1",
            "results.user.sha256",
            "results.user.username")

finaldf.printSchema()
finaldf.show()

procdf = finaldf.withColumn("username", regexp_replace(col("username"), "([0-9])", ""))
procdf.show()

procdf.write.format("csv").mode("overwrite").save("/home/mohan/airflowproj/procdata")

