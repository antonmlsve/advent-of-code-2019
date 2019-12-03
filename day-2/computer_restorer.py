def get_program_output(instructions, noun, verb):
    instructions[1] = noun
    instructions[2] = verb
    parameters_in_single_instruction = 4
    instruction_iterator = [iter(instructions)] * parameters_in_single_instruction
    parameters_grouped_by_instruction = zip(*instruction_iterator)
    for instruction_parameter_group in parameters_grouped_by_instruction:
        instruction_type = instruction_parameter_group[0]
        position_to_get_number_from_1 = instruction_parameter_group[1]
        position_to_get_number_from_2 = instruction_parameter_group[2]
        position_to_write_to = instruction_parameter_group[3]
        if instruction_type == 1:
            instructions[position_to_write_to] = instructions[position_to_get_number_from_1] + instructions[position_to_get_number_from_2]
        elif instruction_type == 2:
            instructions[position_to_write_to] = instructions[position_to_get_number_from_1] * instructions[position_to_get_number_from_2]
        elif instruction_type == 99:
            break
        else:
            print("ERROR")
            break
    return instructions[0]


def get_input_for_desired_program_output(desired_output, instructions):
    for noun in range(100):
        for verb in range(100):
            program_ouput = get_program_output(instructions.copy(), noun, verb)
            if program_ouput == desired_output:
                return (noun, verb)
    return "No solution found"


if __name__ == "__main__":
    input_file = open("data/input.txt", "r")
    instructions = input_file.read().split(',')
    instructions = list(map(int, instructions))
    noun = 12
    verb = 2
    program_output_task_1 = get_program_output(instructions.copy(), noun, verb)
    print("The input from task 1 produces the computer output: " + str(program_output_task_1) + "\n\n")

    desired_program_output = 19690720
    program_input = get_input_for_desired_program_output(desired_program_output, instructions)
    program_input_for_desired_answer_task_2 = 100 * program_input[0] + program_input[1]
    print("In task 2, the desired programoutput " + str(desired_program_output)
          + " is yielded when when using the verb " + str(program_input[0])
          + " and the noun " + str(program_input[1])
          + "\nTo give: 100 * verb + noun = " + str(program_input_for_desired_answer_task_2))