import ast
import multiprocessing as mp;


class ForLoop:

    def __init__(self, initial_line_number, final_line_number):
        self.initial_line_number = initial_line_number
        self.final_line_number = final_line_number


allForLoops = []
with open("../examples/sum.py") as fin:
    tree = ast.parse(fin.read())
for x in ast.walk(tree):
    if isinstance(x, ast.For):
        print(x.lineno)
        print(x.body[-1].lineno)
        allForLoops.append(ForLoop(x.lineno, x.body[-1].lineno))
print('All loops')
for a in allForLoops:

    print(a.initial_line_number, a.final_line_number)
