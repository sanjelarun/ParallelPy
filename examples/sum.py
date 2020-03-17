## For AST analysis for ParallelPy
def sum_array(numbers):
    sum_all = 0
    sum_a = 0
    for n in numbers:
        sum_all += n
    for n in numbers:
        sum_a -= n
    return sum_all

## For AST information
def no_loop():
    print("Hello")


numbers = [1, 2, 3, 4, 5, 5, 10, 12]
print(sum_array(numbers))
