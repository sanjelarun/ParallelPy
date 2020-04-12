import ast
from parallelpy.modules.models import LoopInformation
from parallelpy.modules.models import OperationInformation
from parallelpy.modules.models import FunctionInformation


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


# Extract  function  then searches for loops in it. Store all loop information
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
def program_analysis(program_information, filepath):
    with open(filepath, "rt") as fin:
        tree = ast.parse(fin.read())
    for x in ast.walk(tree):
        if isinstance(x, ast.FunctionDef):
            function_info = funtion_analysis(x)
            program_information.all_functions.append(function_info)
