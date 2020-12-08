
def maxNum(numbers):
    max1 = 0
    for n in numbers:
        if n > max1:
            max1 = n
    return max1

def test_case():
    assert maxNum([1,2,3,4]) == 4
