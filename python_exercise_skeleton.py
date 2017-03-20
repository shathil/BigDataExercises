"""
Student Name :
Student ID   :
INFORMATION  : http://blogs.helsinki.fi/alakopsaa/processing-a-suspicion-of-cheating/?lang=en
"""
from __future__ import print_function
from pyspark import SparkContext, SparkConf

class ExerciseSet2(object):
    """
    Big Data Frameworks Exercises
    https://www.cs.helsinki.fi/courses/582740/2017/k/k/1
    """

    def __init__(self):
        """
        Initializing Spark Conf and Spark Context here
        Some Global variables can also be initialized
        """
        self.conf = (SparkConf().setMaster("local").
                     setAppName("exercise_set_2").
                     set("spark.executor.memory", "2g"))
        self.spark_context = SparkContext(conf=self.conf)
        # Have global variables here if you wish
        # self.global_variable = None

    def exercise_1(self):
        """
        # Write your Docstring here
        """
        # self.spark_context
        # samplerdd = self.spark_context.parallelize([2,3,4,5])
        return None

    def exercise_2(self):
        """
        # Write your Docstring here
        """
        # self.spark_context
        return None

    def exercise_3(self):
        """
        # Write your Docstring here
        """
        # self.spark_context
        return None

    def exercise_4(self):
        """
        # Write your Docstring here
        """
        # self.spark_context
        return None

    def exercise_5(self):
        """
        # Write your Docstring here
        """
        # self.spark_context
        return None

    def exercise_6(self):
        """
        # Write your Docstring here
        """
        # self.spark_context
        return None

if __name__ == "__main__":
    EXERCISESET2 = ExerciseSet2()
    EXERCISESET2.exercise_1()
    EXERCISESET2.exercise_2()
    EXERCISESET2.exercise_3()
    EXERCISESET2.exercise_4()
    EXERCISESET2.exercise_5()
    EXERCISESET2.exercise_6()
