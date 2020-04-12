class ProgramInformation:
    def __init__(self):
        self.all_functions = []


# Store all function information
class FunctionInformation:

    def __init__(self):
        self.name = []
        self.iteration = []
        self.input_variable = []
        self.return_variable = [] # TODO:  add return type for generation
        self.return_type = ""


# Store all loop information [Right now it is only for loop]
class LoopInformation:

    def __init__(self, initial_line_number, final_line_number):
        self.loop_variables = ''
        self.allVariables = []
        self.initial_line_number = initial_line_number
        self.final_line_number = final_line_number
        self.operations = []
        self.conditions = []
        self.mainOperation = ""
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


# Stores all replace line information
class LoopReplace:
    def __init__(self,initial_line_no,final_line_number,replace_strings):
        self.initial_line_no = initial_line_no
        self.final_line_number = final_line_number
        self.replace_strings =replace_strings
