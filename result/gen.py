import pyspark as ps

## For AST analysis for ParallelPy
def check(n1):
    n1 = n1 + 2
    n1 = n1 * 3
    return n1

def sum_array(numbers):
    sc = ps.SparkContext()
    numbers_RDD_0 = sc.parallelize(numbers)
    numbers_RDD_1 = numbers_RDD_0.map(lambda n1: n1+2)
    numbers = numbers_RDD_1.map(lambda n1: n1*3)
    return numbers.collect()

numbers = [1, 52, 3, 4, 5, 5, 10, 12]
print(sum_array(numbers))

