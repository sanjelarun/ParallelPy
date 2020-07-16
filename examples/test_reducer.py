

def check(a, n1):
    return a + n1

def sum_array(numbers):
    num = 0
    for n in numbers:
       num = check(num, n)
    return num

numbers = [1, 52, 3, 4, 6, 5, 10]
print(sum_array(numbers))

 # re = final.map(lambda x: (1,(x[0],x[1]))).reduceByKey(lambda x,y :  (((x[0] * y[1])+y[0])/(y[1]+1), 0))