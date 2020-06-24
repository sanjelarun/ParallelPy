import ast
from parallelpy.modules.udf_models import CustomLoopInformation
from parallelpy.modules.codegen_udf import *
def udf_calls(node, call_type, final_target, filepath, intial_num, final_num):
    print("The Loop has UDF calls")
    customNode = CustomLoopInformation(call_type)
    customNode.check_for_filter(node)
    customNode.classify_udf(node)
    final_gen = codegen_complete_mapper(final_target, customNode.mapper_list.mr_steps)
    print(*final_gen, sep="\n")
    code_gen_file(filepath, intial_num, final_num, final_gen)
    # customNode.getInputVariables(node)
    # customNode.getOperators(node)
    return

