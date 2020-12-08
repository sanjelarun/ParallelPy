

def check(a, n1):
    return a + n1

def sum_array(numbers):
    num = 0
    for n in numbers:
       num = check(num, n)
    return num

def test_1():
    expected = 6
    result = sum_array([1,2,3])
    assert result == expected
def test_wrong():
    expected = 8
    result = sum_array([1,2,3,4])
    assert result != expected
def test_2():
    expected = -45
    result = sum_array([10,-50,2,3,-10,7,8,-15])
    assert result == expected


 # re = final.map(lambda x: (1,(x[0],x[1]))).reduceByKey(lambda x,y :  (((x[0] * y[1])+y[0])/(y[1]+1), 0))