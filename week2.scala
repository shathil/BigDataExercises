/**
 * @author Name StudentNo
 */

package bdf.exercises

import org.apache.spark._
import org.apache.spark.SparkContext._


object week2 {
  /**
   * Big Data Frameworks Exercises
   * https://courses.helsinki.fi/en/data14001/124845011
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
    val conf = new SparkConf().setAppName("week2").setMaster("local")
    val sc = new SparkContext(conf)
    /* Run exercise1 code */
    exercise1(sc)
    /* Run exercise2 code */
    exercise2(sc)
    /* Run exercise3 code */
    exercise3(sc)
    /* Run exercise4 code */
    exercise4(sc)
    /* Run exercise5 code */
    exercise5(sc)
    /* Run exercise6 code */
    exercise6(sc)
    /* Stop the sc */
    sc.stop()
  }

}
