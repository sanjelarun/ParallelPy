import ast
from parallelpy.modules.udf_models import CustomLoopInformation
def udf_calls(node, call_type):
    print("The Loop has UDF calls")
    customNode = CustomLoopInformation(call_type)
    customNode.check_for_filter(node)
    customNode.classify_udf(node)

    # customNode.getInputVariables(node)
    # customNode.getOperators(node)
    return

