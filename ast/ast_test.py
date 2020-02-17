import ast
import multiprocessing as mp;

with open("../examples/sum.py") as fin:
    tree = ast.parse(fin.read())
for x in ast.walk(tree):
    if isinstance(x, ast.For):
        print(x.lineno)
        print(x.body[-1].lineno)

print(mp.cpu_count())