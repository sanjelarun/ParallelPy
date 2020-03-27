import pyspark as ps


def sum_array(numbers):
    sum_all = 0
    sum_all_RDD = sc.parallelize(numbers)
    sum_all=sum_all_RDD.map().reduce(lambda accum, num: accum + num)
    return sum_all


sc = ps.SparkContext()

numbers = [1, 2, 3, 4, 5, 5, 10, 12]
print(sum_array(numbers))
