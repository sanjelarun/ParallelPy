

def check(num, i, n):
    return ((num * i) + n) / (i + 1)


def sum_array(numbers):
    num = 0
    b = list(range(len(numbers)))
    print(b)
    for i in b:
        num = check(num, i, numbers[i])
        #print(num)
    return num

numbers = [1, 52, 3, 4, 6, 5, 10]
print(sum_array(numbers))

# re = final.map(lambda x: (1, (x[0], x[1]))).reduceByKey(lambda x, y: (((x[0] * y[1]) + y[0]) / (y[1] + 1), 0))