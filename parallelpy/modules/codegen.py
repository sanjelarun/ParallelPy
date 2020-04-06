import ast
from parallelpy.modules.models import LoopReplace


# Lets start codegen with no verification or anything just to test the my analysis works or not
def mapper_reducer_generation(program_information):
    list_of_new_operations = []
    s = ''
    initial_number = 0
    final_number = 0
    for functions in program_information.all_functions:
        for iteration in functions.iteration:
            initial_number = iteration.initial_line_number
            final_number = iteration.final_line_number
            for ops in iteration.operations:
                if isinstance(ops.op, ast.Add):
                    changeRDD = ops.left + '_RDD = sc.parallelize(' + 'numbers' + ')'
                    list_of_new_operations.append(changeRDD)
                    s += ops.left +'='+ops.left +'_RDD.map(lambda x:(1, x)).reduceByKey(lambda accum, num: accum + num).collect()'
                    list_of_new_operations.append(s)
                    s = ''
    return LoopReplace(initial_number, final_number, list_of_new_operations)

def reducerLine(operations): # type : parallelpy.models.Operation information):
    accum = ""
    num = ""
    # if operations.left
    # return "reduceByKey(lambda" + accum+ "," num: accum + num)"
# Code Gen Portion
def codeGen(replace):
    fin = open("../examples/test.py","rt")
    fout = open("../result/gen.py","wt")
    cnt = 0
    fout.write("import pyspark as ps")
    for i,line in enumerate(fin):
        if not (replace.initial_line_no <= i+1 <= replace.final_line_number):
            fout.write(line)
        else:
            if cnt == 0:
                fout.write("    sc = ps.SparkContext()\n")
            fout.write("    "+replace.replace_strings[cnt]+"\n")
            cnt+=1
