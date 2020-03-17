import ast


## Store Program information
class ProgramInformation:
    def __init__(self):
        self.functions: []


## Store all function information
class FunctionInformation:

    def __init__(self):
        self.name = []
        self.iteration = []
        self.input_variable = []
        self.return_type = ""


## Store all loop information [Right now it is only for loop]
class LoopInformation:

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


def extracted_loops(node):
    ## Extraction Phase
    allForLoops = []
    for x in ast.walk(node):
        if isinstance(x, ast.For):
            temp_f = LoopInformation(x.lineno, x.body[-1].lineno)
            for node in ast.walk(x):
               ## print(node)
                if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                    if not temp_f.allVariables.__contains__(node.id):
                        temp_f.add_variables(node.id)
                if isinstance(node, ast.Add):
                    print(node)
                    ## temp_f.add_operations(node.operator)
            allForLoops.append(temp_f)
    print('All loops')
    for a in allForLoops:
        print(a.initial_line_number, a.final_line_number)
        print(a.allVariables)
        print(a.operations)


def funtion_analysis(node):
    for x in ast.walk(node):
        extracted_loops(x)


def program_analysis():
    with open("../examples/sum.py") as fin:
        tree = ast.parse(fin.read())
    for x in ast.walk(tree):
        print(x)
        if isinstance(x, ast.FunctionDef):
            print("here")
            funtion_analysis(x)


def main():
    program_analysis()


if __name__ == "__main__":
    main()
