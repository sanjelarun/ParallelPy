

def check(a, n1):
    return a + n1

def sum_array(numbers):
    num = 0
    for n in numbers:
       num = check(num, n)
    return num

numbers = [1, 52, 3, 4, 6, 5, 10, 12]
print(sum_array(numbers))