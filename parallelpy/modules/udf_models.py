import ast
from parallelpy.modules.models import VariableInformation

# Stores Codegen Stuff
class CodeGen:
    def __init__(self):
        self.mr_steps = []


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
    def __init__(self, left, right, target,operations, operator):
        self.left = left
        self.right = right
        self.target = target
        self.operation = operations
        self.operator = operator


# New Function information
class CustomLoopInformation:

    loopVariable = set()
    udf_call_type = ""
    filter_info = FilterInformation()
    def __init__(self, call_type):
        print(call_type)
        self.udf_call_type = call_type


    def check_for_filter(self, exp):
        if exp is None:
            return
        else:
            for tmp in ast.walk(exp):
              if isinstance(tmp, ast.If):
                  self.filter_info.has_if = True

    def get_all_if_cases(self, exp):
        return

    def mapper_binary_ops(self, exp):
        print("Mapper with Filter")
        return

    def mapper_only(self, exp):
        print("Mapper Only")
        return

    def reducer_binary_ops (self, exp):
        print ("Mapper and Reducer")
        return

    def classify_udf(self, node,):
        if self.udf_call_type is "mExpression" and self.filter_info.has_if is False:
            self.mapper_only(node)
        elif self.udf_call_type is "mExpression" and self.filter_info.has_if is True:
            self.mapper_binary_ops(node)
        else:
            self.reducer_binary_ops(node)
