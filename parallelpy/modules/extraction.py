import ast
from parallelpy.modules.models import *


# Return First and Last Linenumber
def _compute_interval(node):
    min_lineno = node.lineno
    max_lineno = node.lineno
    for node in ast.walk(node):
        if hasattr(node, "lineno"):
            min_lineno = min(min_lineno, node.lineno)
            max_lineno = max(max_lineno, node.lineno)
    return min_lineno, max_lineno


# check Number
def variable_check(operand):
    if isinstance(operand, ast.Name):
        return operand.id
    elif isinstance(operand, ast.Num):
        return operand.n


# Extracts all loops from a function node
def extracted_loops(node):
    if isinstance(node, ast.For):
        min_line_no, max_line_no = _compute_interval(node)
        temp_f = LoopInformation(min_line_no, max_line_no)
        has_compare = check_for_compare(node)
        for node in ast.walk(node):
            # print(node) get all variables
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                if not temp_f.allVariables.__contains__(node.id):
                    print(node.id)
                    temp_f.add_variables(node.id)
            # Only for Sum and Count
            if not has_compare:
                if isinstance(node, ast.Assign):
                    print(node)
                    if isinstance(node.value, ast.BinOp):
                        left = variable_check(node.value.left)
                        op = node.value.op
                        right = variable_check(node.value.right)
                        target = node.targets[0].id
                        if target != left:
                            temp = left
                            left = right
                            right = temp
                        print(left, op, right, target)
                        if right == "1" or right == 1:
                            temp_f.add_operations(OperationInformation(left, op, right, target, "COUNT"))
                        else:
                            temp_f.add_operations(OperationInformation(left, op, right, target, "ADD"))
            else:
                if isinstance(node, ast.If):
                    compare_info = CompareInformation(node.test.left.id, node.test.ops[0], node.test.comparators[0].id )
                    temp_f.add_comapre_information(compare_info)
                    print(compare_info)
                    for ifbody in node.body:
                        if isinstance(ifbody, ast.Assign):
                            target = ifbody.targets[0].id
                            if isinstance(compare_info.ops,ast.Lt):
                                temp_f.add_operations(OperationInformation(target, compare_info.ops, "", target,"MAX"))
                            else:

                                temp_f.add_operations(OperationInformation(target, compare_info.ops, "", target,"MIN"))
        return temp_f
    return -1


# Check if  For Loop has if or any condition
def check_for_compare(node):
    for tmp in ast.walk(node):
        if isinstance(tmp, ast.Compare):
            return True
    return False


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


# Convert expression extracted to standard one
def convert_expression_to_standard():
    return ""
