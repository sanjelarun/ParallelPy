import pyspark as ps
def alter_values(data_1, data_2):
    sc = ps.SparkContext()
    data_1_RDD = sc.parallelize(data_1)
    data_2_RDD = sc.parallelize(data_2)
    data_1_RDD_combine =data_1_RDD.join(data_2_RDD)
    data_1_RDD_combine =data_1_RDD_combine.map(lambda x: (x[0],x[1][0]+x[1][1])).collect()
    return data_1_RDD_combine


data1 = [('a',1), ('b',52), ('c',3)]
data2 = [('a',2), ('b',3), ('c',4)]
print(alter_values(data1, data2))
