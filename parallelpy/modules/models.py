import ast
# Store Program information
from typing import Set, Any


class ProgramInformation:
    def __init__(self):
        self.all_functions = []

    def get_function_node_by_name(self, name):
        for tmp in self.all_functions:
            if tmp.name == name:
                return tmp.node


# Store all function information
class FunctionInformation:

    def __init__(self, node):
        self.name = ""
        self.iteration = []
        self.input_variable = []
        self.return_variable = []  # TODO:  add return type for generation
        self.node = node
        self.return_type = ""


# Store all loop information [Right now it is only for loop]
class LoopInformation:

    def __init__(self, initial_line_number: int, final_line_number: int):
        self.loop_variables = ''
        self.allVariables = []
        self.initial_line_number = initial_line_number
        self.final_line_number = final_line_number
        self.operations = []
        self.conditions = []
        self.mainOperations = ""
        self.compareInformation = []

    def add_conditions(self, condition):
        self.conditions.append(condition)

    def add_operations(self, operation):
        self.operations.append(operation)

    def add_variables(self, variable):
        self.allVariables.append(variable)

    def add_comapre_information(self, compare_info):
        self.compareInformation.append(compare_info)


# Operation information stored in (left, op,  right)
class OperationInformation:

    def __init__(self, left, op, right, target, main_ops):
        self.left = left
        self.op = op
        self.right = right
        self.target = target
        self.ops = main_ops


# Stores all if/else condition for us
class CompareInformation:

    def __init__(self, left, ops, compare):
        self.left = left
        self.ops = ops
        self.compare = compare


# Stores all replace line information
class LoopReplace:
    def __init__(self, initial_line_no, final_line_number, replace_strings):
        self.initial_line_no = initial_line_no
        self.final_line_number = final_line_number
        self.replace_strings = replace_strings


# FOR UDF we need to search for summary and grammar
class SearchConfig:
    def __init__(self):
        self.inbits = 2
        self.arraySize = 4
        self.intRange = 4
        self.loopUnrolled = 4

        self.maxMR = 5
        self.maxEmits = 5
        self.maxTuple = 5
        self.maxRecursionDept = 5


# Variable Information
class VariableInformation:
    def __init__(self, varName, varType):
        self.varName = varName
        self.varType = varType


# New Function information
class CustomLoopInformation:
    inputVariables = []
    operators = set()
    expressions = set()
    loopVariable = set()

    def check_fo_exp(self, expression):

        if isinstance(expression, ast.AugAssign):
            self.operators.add(expression.op)
        elif isinstance(expression, ast.If):
            for tmp in expression.test.ops:
                self.operators.add(tmp)
        elif isinstance(expression.value, ast.UnaryOp):
            self.operators.add(expression.value.op)
        elif isinstance(expression.value, ast.BinOp):
            self.operators.add(expression.value.op)

    def getInputVariables(self, exp):
        if exp is None:
            return
        else:
            for node in ast.walk(exp):
                if isinstance(node, ast.Name):
                    var = VariableInformation(node.id, "V")
                    if var not in self.inputVariables:
                        self.inputVariables.append(var)

    def getOperators(self, exp):
        if exp is None:
            return
        else:
            for node in ast.walk(exp):
                if isinstance(node, ast.Assign) or isinstance(node, ast.AugAssign) or isinstance(node, ast.If):
                    self.check_fo_exp(node)
