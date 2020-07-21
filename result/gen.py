import pyspark as ps
from math import sqrt
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1) - 1):
        distance = distance + (row1[i] - row2[i]) ** 2
    return sqrt(distance)


# Locate the most similar neighbors
def get_neighbors(train, test_row):
    distances = list()
    sc  = ps.SparkContext()
    train_RDD = sc.parallelize(train)
    train_RDD = train_RDD.map(lambda x: (x,euclidean_distance(x, test_row))).collect()
    print(train_RDD)
    # for train_row in train:
    #     dist = euclidean_distance(test_row, train_row)
    #     distances.append((train_row, dist))
    # return distances
    return train_RDD
# Test distance function
dataset = [[2.7810836, 2.550537003, 0],
           [1.465489372, 2.362125076, 0],
           [3.396561688, 4.400293529, 0],
           [1.38807019, 1.850220317, 0],
           [3.06407232, 3.005305973, 0],
           [7.627531214, 2.759262235, 1],
           [5.332441248, 2.088626775, 1],
           [6.922596716, 1.77106367, 1],
           [8.675418651, -0.242068655, 1],
           [7.673756466, 3.508563011, 1]]
test_point = dataset[0]
neighbors = get_neighbors(dataset, test_point)
neighbors.sort(key=lambda tup: tup[1])
print(neighbors[:3])
# re = final.map(lambda x: (1, (x[0], x[1]))).reduceByKey(lambda x, y: (((x[0] * y[1]) + y[0]) / (y[1] + 1), 0))