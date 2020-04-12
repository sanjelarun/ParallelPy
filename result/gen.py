import pyspark as ps

## For AST analysis for ParallelPy
def sum_array(numbers):
    sum_all = 0
    sc = ps.SparkContext()
    sum_all_RDD = sc.parallelize(numbers)
    sum_all=sum_all_RDD.sum()
    return sum_all


numbers = [1, 2, 3, 4, 5, 5, 10, 12]
print(sum_array(numbers))
