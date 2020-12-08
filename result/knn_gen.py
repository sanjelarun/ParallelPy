from math import sqrt
import pyspark as ps

# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
    distance = (row1[0] - row2[0]) ** 2 + (row1[1] - row2[1])**2
    return sqrt(distance)

# Get distance of points in the dataset
def get_neighbors(train, test_row):
    distances = []
    sc = ps.SparkContext()
    train_RDD = sc.parallelize(train)
    distances = train_RDD.map(lambda train_row: (euclidean_distance(train_row,test_row),train_row)).collect()
    sc.stop()
    return distances

# Return Only K nearest neighbours, no any classification or regression done right now
def KNN(data, query, k):
    data_list = get_neighbors(data,query)
    sortedData = data_list.sortByKey().take(k)
    return  sortedData


dataset = [[2.7810836, 2.550537003],
           [1.465489372, 2.362125076],
           [3.396561688, 4.400293529],
           [1.38807019, 1.850220317],
           [3.06407232, 3.005305973],
           [7.627531214, 2.759262235],
           [5.332441248, 2.088626775],
           [6.922596716, 1.77106367],
           [8.675418651, -0.242068655],
           [7.673756466, 3.508563011]]

# def test1():
#     knn_result = KNN(dataset, [3.2,1.2],3)
#     assert  len(knn_result) == 3
# def test_wrong():
#     knn_result = KNN(dataset, [3.2,1.2],3)
#     expected = [(1.392838827718412, [2.7, 2.5])]
#     assert  knn_result != expected
# def test2():
#     knn_result = KNN(dataset, [3.2, 1.2], 5)
#     expected = [(1.392838827718412, [2.7, 2.5]),
#                 (1.8110770276274835, [3.0, 3.0]),
#                 (1.9924858845171276, [1.3, 1.8]),
#                 (2.109502310972899, [1.4, 2.3]),
#                 (2.276927754672949, [5.3, 2.08])]
#     assert  knn_result == expected