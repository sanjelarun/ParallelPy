from parallelpy.modules import codegen, extraction, models


def main():
    filepath = "../examples/test.py"
    program_information = models.ProgramInformation()
    extraction.program_analysis(program_information, filepath)
    codegen.codeGen(codegen.mapper_reducer_generation(program_information))
    for temp in program_information.all_functions:
        print(temp.name)


if __name__ == "__main__":
    main()
