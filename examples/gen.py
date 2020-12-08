import pyspark as ps
import time
## For AST analysis for ParallelPy
def sum_array(numbers):
    sum_all = 0
    sc = ps.SparkContext()
    sc.setLogLevel('WARN')
    se = time.time()
    sum_all_RDD = sc.textFile(numbers).map(lambda x: x.split(",")).flatMap(lambda  x : x).map(lambda x: int(x))
    sum_all=sum_all_RDD.sum()
    print(time.time() - se)
    sc.stop()
    return sum_all



filen = "1.csv"
print(sum_array(filen))