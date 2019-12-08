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


def run_program_async(program, **kwargs):
    program = list(program)  # Make a copy because we mutate it.
    program_input = kwargs.get('program_input', [])
    program_output = kwargs.get('program_output', [])
    program_state = 'RUNNING'
    pos = kwargs.get('instruction_ptr', 0)

    def state():
        return {
            'program': program,
            'program_input': program_input,
            'program_output': program_output,
            'instruction_ptr': pos,
            'status': program_state,
        }

    while True:
        if program[pos] == 99:
            program_state = 'FINISHED'
            break

        op_code, parameters = parse_operation(program, pos)

        if op_code == 1:
            program[program[pos + 3]] = parameters[0] + parameters[1]
            pos += 4
        elif op_code == 2:
            program[program[pos + 3]] = parameters[0] * parameters[1]
            pos += 4
        elif op_code == 3:
            if not program_input:
                program_state = 'NEEDS_INPUT'
                return state()
            program[program[pos + 1]] = program_input.pop(0)
            pos += 2
        elif op_code == 4:
            program_output.append(parameters[0])
            pos += 2
            program_state = 'GENERATED_OUTPUT'
            return state()
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
    return state()


def run_program(program, program_input=None):
    state = run_program_async(program, program_input=program_input)
    while state['status'] != 'FINISHED':
        state = run_program_async(**state)
    return state


def run_amplifiers_in_series(amp_ctrl, phase_settings):
    output_signal = 0
    for phase in phase_settings:
        result = run_program(amp_ctrl, program_input=[phase, output_signal])
        output_signal = result['program_output'][0]
    return output_signal


def run_amplifiers_in_loop(amp_ctrl, phase_settings):
    amplifier_state = [{}, {}, {}, {}, {}]
    # Kick off all amps with initial input.
    for index, phase in enumerate(phase_settings):
        program_input = [phase]
        # Second input to first amp is zero.
        if index == 0:
            program_input.append(0)
        amplifier_state[index] = run_program_async(amp_ctrl, program_input=program_input)
    # Run amps until finished, moving any output to its respective input.
    while any([amp['status'] != 'FINISHED' for amp in amplifier_state]):
        for amp_num in range(5):
            amp = amplifier_state[amp_num]
            if amp['status'] == 'GENERATED_OUTPUT':
                amp_num_for_output = 0 if amp_num == 4 else amp_num + 1
                amplifier_state[amp_num_for_output]['program_input'].append(amp['program_output'][-1])
                amplifier_state[amp_num] = run_program_async(**amp)
            elif amp['status'] == 'NEEDS_INPUT' and amp['program_input']:
                amplifier_state[amp_num] = run_program_async(**amp)
    return amplifier_state[4]['program_output'][-1]


def generate_permutations(digit_start, digit_end):
    for a in range(digit_start, digit_end + 1):
        for b in range(digit_start, digit_end + 1):
            for c in range(digit_start, digit_end + 1):
                for d in range(digit_start, digit_end + 1):
                    for e in range(digit_start, digit_end + 1):
                        combination = [a, b, c, d, e]
                        if len(set(combination)) != 5:
                            continue
                        yield combination


if __name__ == '__main__':
    puzzle_input = [int(i) for i in open('day_7.in').read().split(',')]

    # Part 1
    assert run_amplifiers_in_series(
        amp_ctrl=[
            3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0
        ],
        phase_settings=[4, 3, 2, 1, 0]
    ) == 43210

    assert run_amplifiers_in_series(
        amp_ctrl=[
            3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23,
            101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0
        ],
        phase_settings=[0, 1, 2, 3, 4]
    ) == 54321

    assert run_amplifiers_in_series(
        amp_ctrl=[
            3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33,
            1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0
        ],
        phase_settings=[1, 0, 4, 3, 2]
    ) == 65210

    print(
        max([
            run_amplifiers_in_series(puzzle_input, combo)
            for combo in generate_permutations(0, 4)
        ])
    )

    # Part 2
    assert run_amplifiers_in_loop(
        amp_ctrl=[
            3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
            27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5
        ],
        phase_settings=[9, 8, 7, 6, 5]
    ) == 139629729

    assert run_amplifiers_in_loop(
        amp_ctrl=[
            3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
            -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
            53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10
        ],
        phase_settings=[9, 7, 8, 5, 6]
    ) == 18216

    print(
        max([
            run_amplifiers_in_loop(puzzle_input, combo)
            for combo in generate_permutations(5, 9)
        ])
    )
