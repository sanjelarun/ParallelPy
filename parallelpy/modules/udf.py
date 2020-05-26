import ast
from parallelpy.modules.models import CustomLoopInformation
def udf_calls(node):
    print("The Loop has UDF calls")
    customNode = CustomLoopInformation()
    customNode.getInputVariables(node)
    customNode.getOperators(node)
    print("All input Variables = ", [a.varName for a  in  customNode.inputVariables])
    print("All operators = ", [a for a in customNode.operators])
    return

