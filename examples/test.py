

## For AST analysis for ParallelPy
def check(n1):
    s = 1
    a = []
    if n1 > 2:
        a[n1] = s + 2
        return n1

def sum_array(numbers):
    a = 0
    sum_all = 0
    for n in numbers:
       sum_all = check(n) + sum_all
    average = sum_all/a
    return average

numbers = [1, 2, 3, 4, 5, 5, 10, 12]
print(sum_array(numbers))

