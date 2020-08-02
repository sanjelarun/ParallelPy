def alter_values(data_1, data_2):
    data_3 = []
    for i in data_1:
        for j in data_2:
            if i[0] == j[0]:
                data_3.append((i[0] , i[1],j[1])) # key, tuple
    return data_3


data1 = [('a',1), ('b',52), ('c',3)]
data2 = [('a',2), ('b',3), ('c',4)]
print(alter_values(data1, data2))
