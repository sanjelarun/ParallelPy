import pyspark as ps

## For AST analysis for ParallelPy
def check(n1):
    s = 1
    if n1 > 2:
        s += 2
        z = 2 - 3
        return n1
    else:
        return 0

def sum_array(numbers):
    a = 0
    sum_all = 0
    sc = ps.SparkContext()
    sum_all_RDD = sc.parallelize(numbers)
    sum_all=sum_all_RDD.sum()
    average = sum_all/a
    return average

numbers = [1, 2, 3, 4, 5, 5, 10, 12]
print(sum_array(numbers))

