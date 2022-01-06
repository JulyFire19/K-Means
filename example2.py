import findspark
findspark.init()
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
import time
from pyspark.sql import SparkSession


starttime = time.time()
# conf = SparkConf()
# sc = SparkContext(conf = conf)

spark = SparkSession.builder.appName("K-Means").getOrCreate()

# 程序主要完成对空间点的聚类，6个空间点x,y,z坐标如下
# 0 1:0.0 2:0.0 3:0.0
# 1 1:0.1 2:0.1 3:0.1
# 2 1:0.2 2:0.2 3:0.2
# 3 1:9.0 2:9.0 3:9.0
# 4 1:9.1 2:9.1 3:9.1
# 5 1:9.2 2:9.2 3:9.2

# Loads data. 注意修改txt文件路径
dataset = spark.read.format("libsvm").load("shuju.txt")

# 训练一个kmeans模型，将K设置为2，将分为两个簇
kmeans = KMeans().setSeed(1).setK(1000)
model = kmeans.fit(dataset)

# 预测 Make predictions
predictions = model.transform(dataset)

# 评估：创建评估器对象及评估 Evaluate clustering by computing Silhouette score
evaluator = ClusteringEvaluator()

silhouette = evaluator.evaluate(predictions)
print("Silhouette with squared euclidean distance = " + str(silhouette))

# 打印中心点Shows the result.
centers = model.clusterCenters()
print("Cluster Centers: ")
for center in centers:
    print(center)
# sc.stop()
endtime = time.time()
print("Runtime:" + str(endtime-starttime))