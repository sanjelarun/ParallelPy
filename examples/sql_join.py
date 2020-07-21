def alter_values(data_1, data_2):
    data_3 = []
    for i in data_1:
        for j in data_2:
            if i == j:
                data_3.append((i, j))
    return data_3


data_1 = [1, 2, 3]
data_2 = [3, 2, 1]
print(data_1, data_2)
print(alter_values(data_1, data_2))
