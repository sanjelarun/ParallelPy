
def codegen_complete_mapper(target, mapper_operations, input_data):
    count = 0
    complete_code = []
    final_RDD =  target +"_RDD_"
    if len(input_data) == 0:
        tmp = final_RDD + str(count) + " = sc.parallelize(" + target + ")"
    else:
        tmp = final_RDD + str(count) + " = sc.parallelize(" + input_data + ")"
    complete_code.append(tmp)
    count += 1
    for each_mapper in mapper_operations[:-1]:
        tmp = final_RDD + str(count) + " = " + final_RDD + str(count - 1) + each_mapper
        count += 1
        complete_code.append(tmp)
    tmp = target + " = " + final_RDD + str(count - 1) + mapper_operations[-1]
    complete_code.append(tmp)
    return complete_code


def codegen_complete_mapper_filter(target, mapper_operations):
    count = 0
    complete_code = []
    final_RDD = target + "_RDD_"
    tmp = final_RDD + str(count) + " = sc.parallelize(" + target + ")"
    complete_code.append(tmp)
    count += 1
    for each_mapper in mapper_operations:
        tmp = final_RDD + str(count) + " = " + final_RDD + "0" + each_mapper
        count += 1
        complete_code.append(tmp)
    s = target + " = " + "sc.union(["
    for i in range(count - 1):
        s += final_RDD + str(i + 1) + ","
    s += "])"
    complete_code.append(s)
    return complete_code


def codegen_complete_reducer(target, mr_operations, input_datset):
    count = 0
    complete_code = []
    final_RDD = target
    tmp = final_RDD + str(count) + " = sc.parallelize(" + input_datset + ")"
    complete_code.append(tmp)
    count += 1
    for each_mapper in mr_operations[:-1]:
        tmp = final_RDD + str(count) + " = " + final_RDD + "0" + each_mapper
        count += 1
        complete_code.append(tmp)
    tmp = final_RDD + " = " + final_RDD + "0" + mr_operations[-1]
    # s = target + " = " + "sc.union(["
    # for i in range(count - 1):
    # s += final_RDD + str(i + 1) + ","
    # s += "])"
    # complete_code.append(s)
    complete_code.append(tmp)
    return complete_code


def codegen_complete_reducer_multiple_mapper(target, list_of_mapper):
    count = 0
    complete_code = []
    final_RDD = target + "_RDD_"
    for i in list_of_mapper:
        tmp = final_RDD + str(count) + " = sc.parallelize(" + i + ")"
        complete_code.append(tmp)
        count += 1
    tmp = final_RDD+str(count) + " = " + final_RDD + str(count - 1) + ".zip(" + final_RDD + "0)"
    complete_code.append(tmp)
    # s = target + " = " + "sc.union(["
    # for i in range(count - 1):
    # s += final_RDD + str(i + 1) + ","
    # s += "])"
    # complete_code.append(s)
    tmp = target + " = " + final_RDD + str(count) + ".map(lambda x: (1, (x[0],x[1]))).reduceByKey(udf).collect()"
    complete_code.append(tmp)
    return complete_code


def write_all(replace, a):
    for s in replace:
        a.write("    " + s + "\n")


def code_gen_file(filepath, intial_num, final_num, codelist, type, function_def=""):
    fin = open(filepath, "rt")
    fout = open("../result/gen.py", "wt")
    cnt = 0
    fout.write("import pyspark as ps\n")
    if type == 5:
        for each in function_def:
            fout.write(each)
    for i, line in enumerate(fin):
        if not (intial_num <= i + 1 <= final_num):
            fout.write(line)
        else:
            if cnt == 0:
                fout.write("    sc = ps.SparkContext()\n")
                for s in codelist:
                    fout.write("    " + s + "\n")
                cnt = 1
