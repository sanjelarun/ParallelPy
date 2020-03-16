import ast


class ForLoop:

    def __init__(self, initial_line_number, final_line_number):
        self.allVariables = []
        self.initial_line_number = initial_line_number
        self.final_line_number = final_line_number
        self.operations = []
        self.conditions = []

    def add_conditions(self, condition):
        self.conditions.append(condition)

    def add_operations(self, operation):
        self.operations.append(operation)

    def add_variables(self, variable):
        self.allVariables.append(variable)


allForLoops = []
with open("../examples/sum.py") as fin:
    tree = ast.parse(fin.read())
for x in ast.walk(tree):
    if isinstance(x, ast.For):
        temp_f = ForLoop(x.lineno, x.body[-1].lineno)
        for node in ast.walk(x):
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                if not temp_f.allVariables.__contains__(node.id):
                    temp_f.add_variables(node.id)
            if isinstance(node, ast.Expr):
                print(node)
                temp_f.add_operations(node.expr)
        allForLoops.append(temp_f)
print('All loops')
for a in allForLoops:
    print(a.initial_line_number, a.final_line_number)
    print(a.allVariables)
    print(a.operations)