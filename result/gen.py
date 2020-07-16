import pyspark as ps
def udf(accum, num): 
	return (( accum[0] * num[1] ) + num[0] ) / ( num[1] + 1 ),0




def sum_array(numbers):
    num = 0
    b = list(range(len(numbers)))
    print(b)
    sc = ps.SparkContext()
    num_RDD_0 = sc.parallelize(b)
    num_RDD_1 = sc.parallelize(numbers)
    num_RDD_2 = num_RDD_1.zip(num_RDD_0)
    num = num_RDD_2.reduce(lambda a,x: a + x[1]+x[0]).collect()
        #print(num)
    return num

numbers = [1, 3, 4, 6, 5, 10, 52]
print(sum_array(numbers))

# re = final.map(lambda x: (1, (x[0], x[1]))).reduceByKey(lambda x, y: (((x[0] * y[1]) + y[0]) / (y[1] + 1), 0))