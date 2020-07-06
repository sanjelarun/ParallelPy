import pyspark as ps

def check(a, n1):
    return a + n1

def sum_array(numbers):
    num = 1
    sc = ps.SparkContext()
    num_RDD_0 = sc.parallelize(numbers)
    num = num_RDD_0.reduce(lambda accum,n1: accum+n1)
    return num

numbers = [1, 52, 3, 4, 6, 5, 10, 12]
print(sum_array(numbers))