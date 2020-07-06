def check(n1, sum_all,i):
    tmp = sum_all * i
    tmp = tmp * n1
    sum_all = tmp / i + 1
    return sum_all

## For AST analysis for ParallelPy
def sum_array(numbers):
    sum_all = 0
    for i,n in enumerate(numbers):
        sum_all = check(n, sum_all, i)
    return sum_all


numbers = [10, 2, 3, 4, 5, 5, 1210, 12]
print(sum_array(numbers))
