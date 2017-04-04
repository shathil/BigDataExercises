import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf

object week2 {
  /**
   * Big Data Frameworks Exercises
   * https://www.cs.helsinki.fi/courses/582740/2017/k/k/1 
   */
  
  def exercise1(sc: SparkContext) = {
    /**
     * Write your Docstring here       
     */
  }
  def exercise2(sc: SparkContext) = {
    /**
     * Write your Docstring here       
     */
  }
  def exercise3(sc: SparkContext) = {
    /**
     * Write your Docstring here       
     */
  }
  def exercise4(sc: SparkContext) = {
    /**
     * Write your Docstring here       
     */
  }
  def exercise5(sc: SparkContext) = {
    /**
     * Write your Docstring here       
     */    
  }
  def exercise6(sc: SparkContext) = {
    /**
     * Write your Docstring here       
     */    
  }
  
  def main(args: Array[String]): Unit =  {   
    val conf = new SparkConf().setAppName("week2").setMaster("spark://m:7077")
	val sc = new SparkContext(conf)


	def f_sign_change(num: Double):Double = {
	num * -1.0
	}

	import util.Random.nextDouble
	var numbers = Seq.fill(1000)(nextDouble)
	print(numbers.getClass)
	val numRDD = sc.parallelize(numbers)
	print(numRDD.getClass)
	print(numRDD.collect().length)
	val mapRDD = numRDD.map(a => (a)*(-1.0) )
	val function_mapRDD = numRDD.map(f_sign_change)
	/* both mapRDD and function_mapRDD has equal values
	 */
	print(mapRDD.first().getClass)
	print(function_mapRDD.collect().length)
    
    /* Run exercise1 code */
    //exercise1(sc)
    /* Run exercise2 code */
    //exercise2(sc)
    /* Run exercise3 code */
    //exercise3(sc)
    /* Run exercise4 code */
    //exercise4(sc)
    /* Run exercise5 code */
    //exercise5(sc)
    /* Run exercise6 code */
    //exercise6(sc)
    /* Stop the sc */
    sc.stop()
  }

}
