import ast


class NestedLoop:

    def __init__(self):
        self.is_join = False
        self.join_key_index = ""
        self.operations = []
        self.data_1 = ""
        self.data_2 = ""

    def add_operations(self, bino):
        self.operations.append(bino)

    def setJoin(self, val: bool):
        self.is_join = val

    def check_join(self, node):
        for tmp in ast.walk(node):
            if isinstance(tmp, ast.For):
                self.data_2 = tmp.iter.id
            if isinstance(tmp, ast.If):
                self.is_join = True
                self.join_key_index = 0




