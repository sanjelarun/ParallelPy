import ast
from parallelpy.modules.codegen_udf import codegen_complete_mapper

from parallelpy.modules.models import VariableInformation

# Stores Codegen Stuff
class MapperCodeGen:
    def __init__(self):
        self.mr_steps = []

    def add_mapper(self, mapper: str):
        self.mr_steps.append(mapper)

# Stores all filter information
class FilterInformation:

    def __init__(self):
        self.filter_condition = []
        self.filter_counter = 1
        self.has_else = False
        self.has_if = False



# Binary Operation Store
class BinOps:
    left = ""
    right = ""
    target = ""
    operation = ""
    operator = ""
    def __init__(self, left, right, target, operator):
        self.left = left
        self.right = right
        self.target = target
        self.operator = operator

    def get_operation_from_operator(self):
        if isinstance(self.operator, ast.Add):
            self.operation = "+"
        elif isinstance(self.operator, ast.Sub):
            self.operation = "-"
        elif isinstance(self.operator, ast.Mult):
            self.operation = "*"
        elif isinstance(self.operator, ast.Div):
            self.operation = "/"

# New Function information
class CustomLoopInformation:

    loopVariable = set()
    udf_call_type = ""
    filter_info = FilterInformation()
    mapper_list= MapperCodeGen()
    def __init__(self, call_type):
        print(call_type)
        self.udf_call_type = call_type

    # check Number
    def variable_check(self, operand):
        if isinstance(operand, ast.Name):
            return operand.id
        elif isinstance(operand, ast.Num):
            return operand.n

    def check_for_filter(self, exp):
        if exp is None:
            return
        else:
            for tmp in ast.walk(exp):
              if isinstance(tmp, ast.If):
                  self.filter_info.has_if = True

    def get_all_if_cases(self, exp):
        return

    def mapper_only_codegen(self, operation : BinOps):
        s = ".map(lambda " + operation.left + ": "+ str(operation.left) + operation.operation + str(operation.right) +")"
        self.mapper_list.add_mapper(s)
        return

    def mapper_filter_ops(self, exp):
        print("Mapper with Filter")
        return

    def mapper_only(self, exp):
        print("Mapper Only")
        for tmp_node in ast.walk(exp):
            if isinstance(tmp_node, ast.BinOp):
                left = self.variable_check(tmp_node.left)
                op = tmp_node.op
                right = self.variable_check(tmp_node.right)
                # target = tmp_node.targets[0].id
                print(left, op, right, "")
                binary_operation = BinOps(left,right,"",op)
                binary_operation.get_operation_from_operator()
                self.mapper_only_codegen(binary_operation)
        return


    def reducer_binary_ops (self, exp):
        print ("Mapper and Reducer")
        return

    def classify_udf(self, node,):
        if self.udf_call_type is "mExpression" and self.filter_info.has_if is False:
            self.mapper_only(node)

        elif self.udf_call_type is "mExpression" and self.filter_info.has_if is True:
            self.mapper_filter_ops(node)
        else:
            self.reducer_binary_ops(node)
