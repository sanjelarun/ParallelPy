import pyspark as ps

## For AST analysis for ParallelPy

def sum_array(numbers):
    a = 0
    sum_all = 0
    sc = ps.SparkContext()
    a_RDD = sc.parallelize(numbers)
    a=a_RDD.count()
    sum_all_RDD = sc.parallelize(numbers)
    sum_all=sum_all_RDD.sum()
    average = sum_all/a
    return average

numbers = [1, 2, 3, 4, 5, 5, 10, 12]
print(sum_array(numbers))
