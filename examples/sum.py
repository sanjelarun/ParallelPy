import csv
import time
## For AST analysis for ParallelPy
def sum_array(numbers):
    sum_all = 0
    for n in numbers:
        sum_all = sum_all + n
    return sum_all


number = []
with open('1.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        row = [ int(i) for i in row]
        number += row
ste = time.time()
print(sum_array(number))
print(time.time() - ste)
