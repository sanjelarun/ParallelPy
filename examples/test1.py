

## For AST analysis for ParallelPy
def sum_array(numbers):
    sum_all = numbers[0]
    for n in numbers:
        if sum_all > n:
            sum_all = n
    return sum_all


numbers = [10, 2, 3, 4, 5, 5, 1210, 12]
print(sum_array(numbers))
