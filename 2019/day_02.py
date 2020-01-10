def run_program(program):
    pos = 0
    while True:
        op_code = program[pos]
        if op_code == 1:
            program[program[pos + 3]] = program[program[pos + 1]] + program[program[pos + 2]]
            pos += 4
        elif op_code == 2:
            program[program[pos + 3]] = program[program[pos + 1]] * program[program[pos + 2]]
            pos += 4
        elif op_code == 99:
            break
    return program


if __name__ == '__main__':
    puzzle_input = [int(i) for i in open('day_02.in').read().split(',')]

    # Part 1
    assert run_program([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
    assert run_program([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert run_program([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

    puzzle_input[1] = 12
    puzzle_input[2] = 2

    print(run_program(list(puzzle_input))[0])

    # Part 2
    for noun in range(0, 100):
        for verb in range(0, 100):
            code = list(puzzle_input)
            code[1] = noun
            code[2] = verb
            output = run_program(code)[0]
            if output == 19690720:
                print(100 * noun + verb)
                break
