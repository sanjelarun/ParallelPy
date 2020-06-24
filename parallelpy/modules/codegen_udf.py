import ast

def codegen_complete_mapper(target, mapper_operations):
    count = 0
    complete_code = []
    final_RDD =  target +"_RDD_"
    tmp = final_RDD + str(count) + " = sc.parallelize(" + target +")"
    complete_code.append(tmp)
    count += 1
    for each_mapper in mapper_operations[:-1]:
        tmp = final_RDD + str(count) + " = " + final_RDD + str(count -1) + each_mapper
        count += 1
        complete_code.append(tmp)
    tmp = target + " = " + final_RDD + str(count - 1) + mapper_operations[-1]
    complete_code.append(tmp)
    return  complete_code


def write_all(replace, a):
    for s in replace:
        a.write("    " + s + "\n")


def code_gen_file(filepath, intial_num, final_num, codelist):
    fin = open(filepath, "rt")
    fout = open("../result/gen.py", "wt")
    cnt = 0
    fout.write("import pyspark as ps")
    for i, line in enumerate(fin):
        if not (intial_num <= i + 1 <= final_num):
            fout.write(line)
        else:
            if cnt == 0:
                fout.write("    sc = ps.SparkContext()\n")
                for s in codelist:
                    fout.write("    " + s + "\n")
                cnt = 1