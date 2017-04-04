from pyspark import SparkConf, SparkContext
conf = (SparkConf().setMaster("spark://m:7077").setAppName("Examples"))
sc = SparkContext(conf=conf)

import numpy as np
import time
import gc
from operator import add



print("\n \n In Millions: ")
numbers_mil = np.random.normal(size=1000000).tolist()
num_milRDD = sc.parallelize(numbers_mil)
start = time.time()
print(num_milRDD.reduce(lambda a, b: a+b))
end = time.time()
print(end - start)
start = time.time()
print(sum(num_milRDD.collect())) # Just to verify :)
end = time.time()
print(end - start)
# Spark seems to be faster than python now. Lets go a 20 million :)
numbers_mil = None
num_milRDD = None # Always clear your memory
gc.collect()
