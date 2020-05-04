

## For AST analysis for ParallelPy

def sum_array(numbers):
    a = 0
    sum_all = 0
    for n in numbers:
        a = a + 1
        sum_all = n + sum_all
    average = sum_all/a
    return average

numbers = [1, 2, 3, 4, 5, 5, 10, 12]
print(sum_array(numbers))

