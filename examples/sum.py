## For AST analysis for ParallelPy
def sum_array(numbers):
    sum_all = 0
    for n in numbers:
        sum_all = sum_all + n
    return sum_all


## For AST information
def no_loop():
    print("Hello")


## Add new function to see my analysis works
def test_func():
    a = [1, 2, 3, 4, 5]
    for i in a:
        a = i + i
        print(i)



numbers = [1, 2, 3, 4, 5, 5, 10, 12]
print(sum_array(numbers))
