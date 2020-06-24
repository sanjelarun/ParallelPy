import ast
from parallelpy.modules.models import *
from parallelpy.modules.udf import udf_calls

# Return First and Last Line number
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
def extracted_loops(node, program_info : ProgramInformation):
    if isinstance(node, ast.For):
        min_line_no, max_line_no = _compute_interval(node)
        temp_f = LoopInformation(min_line_no, max_line_no)
        has_compare = check_for_compare(node)
        for v_node in ast.walk(node):
            # print(node) get all variables
            if isinstance(v_node, ast.Call) and v_node.func.id is not "enumerate":
                funcName = v_node.func.id
                assignmentInfo = node.body.pop(0)
                if isinstance(assignmentInfo.targets[0], ast.Name):
                    final_target = assignmentInfo.targets[0].value.id
                    udf_calls(program_info.get_function_node_by_name(funcName), "rExpression",final_target, program_info.filepath, min_line_no, max_line_no)
                else:
                    final_target = assignmentInfo.targets[0].value.id
                    udf_calls(program_info.get_function_node_by_name(funcName), "mExpression", final_target, program_info.filepath, min_line_no, max_line_no)
                break
            if isinstance(v_node, ast.Name) and isinstance(v_node.ctx, ast.Store):
                if not temp_f.allVariables.__contains__(v_node.id):
                    print(v_node.id)
                    temp_f.add_variables(v_node.id)
            # Only for Sum and Count
            if not has_compare:
                if isinstance(v_node, ast.Assign):
                    print(v_node)
                    if isinstance(v_node.value, ast.BinOp):
                        left = variable_check(v_node.value.left)
                        op = v_node.value.op
                        right = variable_check(v_node.value.right)
                        target = v_node.targets[0].id
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
                if isinstance(v_node, ast.If):
                    compare_info = CompareInformation(v_node.test.left.id, v_node.test.ops[0], v_node.test.comparators[0].id)
                    temp_f.add_comapre_information(compare_info)
                    print(compare_info)
                    for ifbody in v_node.body:
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
def funtion_analysis(node, progam_info):
    if isinstance(node, ast.FunctionDef):
        function_info = FunctionInformation(node)
        function_info.name = node.name
        for x in ast.walk(node):
            loop_information = extracted_loops(x, progam_info)
            if loop_information != -1:
                function_info.iteration.append(loop_information)
        # for x in function_info.iteration:
        #     print(x.initial_line_number)
        #     print(x.final_line_number)
        #     print(x.allVariables)
        return function_info


# Walks for finding various functions
def program_analysis(program_information : ProgramInformation, filepath):
    program_information.set_filepath(filepath)
    with open(filepath, "rt") as fin:
        tree = ast.parse(fin.read())
    for x in ast.walk(tree):
        if isinstance(x, ast.FunctionDef):
            function_info = funtion_analysis(x, program_information)
            program_information.all_functions.append(function_info)


# Convert expression extracted to standard one
def convert_expression_to_standard():
    return ""
