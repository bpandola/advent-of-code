def parse_op_code(code):
    if len(str(code)) <= 2:
        return int(code), [0, 0, 0]
    str_code = '00000' + str(code)
    return int(str_code[-2:]), [int(str_code[-3]), int(str_code[-4]), int(str_code[-5])]


def parse_operation(program, pos):
    op_code, parameter_modes = parse_op_code(program[pos])
    pos += 1
    parameters = []
    for index, mode in enumerate(parameter_modes):
        parameter = None
        try:
            parameter = program[pos + index] if mode else program[program[pos + index]]
        except IndexError:
            pass
        finally:
            parameters.append(parameter)
    return op_code, parameters


def run_program(program, program_input=None):
    program = list(program)  # Make a copy because we mutate it.
    program_output = []
    pos = 0
    while True:
        if program[pos] == 99:
            break

        op_code, parameters = parse_operation(program, pos)

        if op_code == 1:
            program[program[pos + 3]] = parameters[0] + parameters[1]
            pos += 4
        elif op_code == 2:
            program[program[pos + 3]] = parameters[0] * parameters[1]
            pos += 4
        elif op_code == 3:
            program[program[pos + 1]] = program_input
            pos += 2
        elif op_code == 4:
            program_output.append(parameters[0])
            pos += 2
        elif op_code == 5:
            pos = parameters[1] if parameters[0] != 0 else pos + 3
        elif op_code == 6:
            pos = parameters[1] if parameters[0] == 0 else pos + 3
        elif op_code == 7:
            program[program[pos + 3]] = 1 if parameters[0] < parameters[1] else 0
            pos += 4
        elif op_code == 8:
            program[program[pos + 3]] = 1 if parameters[0] == parameters[1] else 0
            pos += 4
    # Output is array of output or the modified program if it didn't explicitly output anything.
    return program_output or program


if __name__ == '__main__':
    puzzle_input = [int(n) for n in open('day_05.in').read().split(',')]

    # Asserts from Day 2
    assert run_program([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert run_program([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert run_program([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert run_program([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

    # Part 1
    assert run_program([3, 0, 4, 0, 99], 99) == [99]
    assert run_program([1002, 4, 3, 4, 33]) == [1002, 4, 3, 4, 99]

    print(run_program(puzzle_input, 1))

    # Part 2
    assert run_program([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 8) == [1]
    assert run_program([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 7) == [0]
    assert run_program([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 9) == [0]
    assert run_program([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 7) == [1]
    assert run_program([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 8) == [0]
    assert run_program([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 9) == [0]
    assert run_program([3, 3, 1108, -1, 8, 3, 4, 3, 99], 7) == [0]
    assert run_program([3, 3, 1108, -1, 8, 3, 4, 3, 99], 8) == [1]
    assert run_program([3, 3, 1108, -1, 8, 3, 4, 3, 99], 9) == [0]
    assert run_program([3, 3, 1107, -1, 8, 3, 4, 3, 99], 7) == [1]
    assert run_program([3, 3, 1107, -1, 8, 3, 4, 3, 99], 8) == [0]
    assert run_program([3, 3, 1107, -1, 8, 3, 4, 3, 99], 9) == [0]
    assert run_program([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], 0) == [0]
    assert run_program([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], 1) == [1]
    assert run_program([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], 0) == [0]
    assert run_program([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], 1) == [1]
    assert run_program(
        [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20,
         4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], 7) == [999]
    assert run_program(
        [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20,
         4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], 8) == [1000]
    assert run_program(
        [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20,
         4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99], 9) == [1001]

    print(run_program(puzzle_input, 5))
