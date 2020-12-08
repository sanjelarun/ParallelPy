import csv
from random import randint

per_row = 100  # number of columns per row to generate
target_size = 1024**3 # 1 GiB, see https://en.wikipedia.org/wiki/Gibibyte
for i in range(10):
    fileName = str(i) + ".csv"
    print(fileName)
    with open(fileName, 'w', newline='') as f_out:
        f_write = csv.writer(f_out)
        while f_out.tell() < target_size:
            row = [randint(-100, 100) for _ in range(per_row)]
            f_write.writerow(row)