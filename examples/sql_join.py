def alter_values(data_1, data_2):
    data_3 = []
    for i in data_1:
        for j in data_2:
            if i[0] == j[0]:
                sum_1 = i[1] + j[1]
                data_3.append((i[0] , sum_1)) # key, tuple
    return data_3

def test1():
    data_1 = [('a', 100), ('b', 3), ('c', 2), ('d', -203)]
    data_2 = [('a', 1), ('b', 103), ('c', 2), ('d', 3)]
    expected = ('a',101)
    result = alter_values(data_1,data_2)
    assert result[0] == expected

def test2():
    data_1 = [('a', 100), ('b', 3), ('c', 2), ('d', -203)]
    data_2 = [('a', 1), ('b', 103), ('c', 2), ('d', 3)]
    expected = ('a',101)
    result = alter_values(data_1,data_2)
    assert result[1] != expected

def test3():
    data_1 = [('a', 100), ('b', 3), ('c', 2), ('d', -203)]
    data_2 = [('a', 1), ('b', 103), ('c', 2), ('d', 3)]
    expected = ('c',4)
    result = alter_values(data_1,data_2)
    assert result[2] == expected