import ast
from parallelpy.modules.udf_models import CustomLoopInformation
from parallelpy.modules.codegen_udf import *


def udf_calls(node, call_type, final_target, filepath, intial_num, final_num, input_dataset=""):
    print("The Loop has UDF calls")
    customNode = CustomLoopInformation(call_type, input_dataset)
    customNode.check_for_filter(node, "")
    type = customNode.classify_udf(node)
    if type is 0:
        final_gen = codegen_complete_mapper(final_target, customNode.mapper_list.mr_steps,"")
    elif type is 1:
        final_gen = codegen_complete_mapper_filter(final_target,customNode.final_codegen_value)
    elif type is 3:
        final_gen = codegen_complete_mapper(final_target, customNode.mapper_list.mr_steps, customNode.input_dataset)
    else:
        final_gen = codegen_complete_reducer(final_target,customNode.final_codegen_value, customNode.input_dataset)
    print(*final_gen, sep="\n")
    code_gen_file(filepath, intial_num, final_num, final_gen)
    # customNode.getInputVariables(node)
    # customNode.getOperators(node)
    return

