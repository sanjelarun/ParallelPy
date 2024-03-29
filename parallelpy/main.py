from modules import codegen, extraction, models


def main():
    filepath = "examples/reducer_main.py"
    program_information = models.ProgramInformation()
    extraction.program_analysis(program_information, filepath)
    #codegen.codeGen(codegen.mapper_reducer_generation(program_information),filepath)
    for temp in program_information.all_functions:
        print(temp.name)


if __name__ == "__main__":
    main()
