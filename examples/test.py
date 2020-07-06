

## For AST analysis for ParallelPy
def check(n1):
    # n1 = n1 + 2
    if n1 > 3:
        n1 = n1 + 2
    elif n1 == 3:
        n1 = n1 * 3
    else:
        n1 = n1 - 2
    return n1

def sum_array(numbers):
    for i,n in enumerate(numbers):
       numbers[i] = check(n)
    return numbers

numbers = [1, 52, 3, 4, 5, 5, 10, 12]
print(sum_array(numbers))

