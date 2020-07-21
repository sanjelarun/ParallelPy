def alter_values(data_1, data_2):
    cnt = 0
    data_3 = [0] * len(data_1)
    for i in data_1:
        for j in data_2:
            data_3[cnt] += (i + j)
        cnt += 1
    return data_3
data_1 = [1,2,3]
data_2 = [3,2,1]
print(data_1,data_2)
print(alter_values(data_1,data_2))
