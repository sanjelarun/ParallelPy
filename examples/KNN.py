from math import sqrt
# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
    distance = (row1[0] - row2[0]) ** 2 + (row1[1] - row2[1])**2
    return sqrt(distance)

# Get distance of points in the dataset
def get_neighbors(train, test_row):
    distances = list()
    for train_row in enumerate(train):
        dist = euclidean_distance(test_row, train_row)
        distances.append((dist,train_row))
    return distances
# Return Only K nearest neighbours, no any classification or regression done right now
def KNN(data, query, k):
    data_list = get_neighbors(data,query)
    sortedData = sorted(data_list)
    return  sortedData[:k]


dataset = [[2.7, 2.5],
           [1.4, 2.3],
           [3.3, 4.4],
           [1.3, 1.8],
           [3.0, 3.0],
           [7.6, 2.7],
           [5.3, 2.08],
           [6.9, 1.7],
           [8.6, -0.2],
           [7.6, 3.5]]

def test1():
    knn_result = KNN(dataset, [3.2,1.2],3)
    assert  len(knn_result) == 3
def test_wrong():
    knn_result = KNN(dataset, [3.2,1.2],3)
    expected = [(1.392838827718412, [2.7, 2.5])]
    assert  knn_result != expected
def test2():
    knn_result = KNN(dataset, [3.2, 1.2], 5)
    expected = [(1.392838827718412, [2.7, 2.5]),
                (1.8110770276274835, [3.0, 3.0]),
                (1.9924858845171276, [1.3, 1.8]),
                (2.109502310972899, [1.4, 2.3]),
                (2.276927754672949, [5.3, 2.08])]
    assert  knn_result == expected