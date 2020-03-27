import ast


## Store Program information
class ProgramInformation:
    def __init__(self):
        self.all_functions = []


## Store all function information
class FunctionInformation:

    def __init__(self):
        self.name = []
        self.iteration = []
        self.input_variable = []
        self.return_variable = [] # TODO:  add return type for generation
        self.return_type = ""


## Store all loop information [Right now it is only for loop]
class LoopInformation:

    def __init__(self, initial_line_number, final_line_number):
        self.loop_variables = ''
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


# Operation information stored in (left, op,  right)
class OperationInformation:

    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

# Extracts all loops from a function node
def extracted_loops(node):
    if isinstance(node, ast.For):
        temp_f = LoopInformation(node.lineno, node.body[-1].lineno)
        for node in ast.walk(node):
            # print(node) get all variables
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                if not temp_f.allVariables.__contains__(node.id):
                    print(node.id)
                    temp_f.add_variables(node.id)
            # Only for Sum Right now
            if isinstance(node, ast.Assign):
                print(node)
                if isinstance(node.value, ast.BinOp):
                    left = node.value.left.id
                    op = node.value.op
                    right = node.value.right.id
                    print(left ,op , right)
                    temp_f.add_operations(OperationInformation(left, op, right))
                # temp_f.add_operations(node.operator)
        return temp_f
    return -1


## Extract  function  then searches for loops in it. Store all loop information
def funtion_analysis(node):
    function_info = FunctionInformation()
    function_info.name = node.name
    for x in ast.walk(node):
        loop_information = extracted_loops(x)
        if loop_information != -1:
            function_info.iteration.append(loop_information)
    # for x in function_info.iteration:
    #     print(x.initial_line_number)
    #     print(x.final_line_number)
    #     print(x.allVariables)
    return function_info


# Walks for finding various functions
def program_analysis(program_information):
    with open("../examples/test.py") as fin:
        tree = ast.parse(fin.read())
    for x in ast.walk(tree):
        if isinstance(x, ast.FunctionDef):
            function_info = funtion_analysis(x)
            program_information.all_functions.append(function_info)

# Lets start codegen with no verification or anything just to test the my analysis works or not
def mapper_reducer_generation(program_information):
    list_of_new_operations = []
    s = ''
    for functions in program_information.all_functions:
        for iteration in functions.iteration:
            for ops in iteration.operations:
                if isinstance(ops.op, ast.Add):
                    changeRDD = ops.left + '_RDD = sc.parallize(' + 'numbers' + ')'
                    list_of_new_operations.append(changeRDD)
                    s += ops.left +'='+ops.left +'_RDD.map(lambda x:(1, x)).reduceByKey(lambda accum, num: accum + num).collect()'
                    list_of_new_operations.append(s)
                    s = ''
    return list_of_new_operations

def main():
    program_information = ProgramInformation()
    program_analysis(program_information)
    for temp in program_information.all_functions:
        print(temp.name)


if __name__ == "__main__":
    main()
