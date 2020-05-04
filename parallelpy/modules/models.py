# Store Program information
class ProgramInformation:
    def __init__(self):
        self.all_functions = []


# Store all function information
class FunctionInformation:

    def __init__(self):
        self.name = []
        self.iteration = []
        self.input_variable = []
        self.return_variable = []  # TODO:  add return type for generation
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

    def add_comapre_information(self,compare_info):
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

    def __init__(self,left, ops, compare):
        self.left = left
        self.ops = ops
        self.compare = compare


# Stores all replace line information
class LoopReplace:
    def __init__(self, initial_line_no, final_line_number, replace_strings):
        self.initial_line_no = initial_line_no
        self.final_line_number = final_line_number
        self.replace_strings = replace_strings



