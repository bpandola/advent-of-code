class OpCode:
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    ADJUST_RELATIVE_PTR = 9
    HALT = 99


class ParamMode:
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class ProgState:
    RUNNING = 'RUNNING'
    GENERATED_OUTPUT = 'GENERATED_OUTPUT'
    NEEDS_INPUT = 'NEEDS_INPUT'
    HALTED = 'HALTED'


def parse_op_code(code):
    if len(str(code)) <= 2:
        return int(code), [0, 0, 0]
    str_code = '00000' + str(code)
    return int(str_code[-2:]), [int(str_code[-3]), int(str_code[-4]), int(str_code[-5])]


def parse_operation(memory, instr_ptr, relative_ptr):
    op_code, parameter_modes = parse_op_code(memory[instr_ptr])
    param_ptrs = []
    for mode in parameter_modes:
        instr_ptr += 1
        param_ptr = None
        try:
            if mode == ParamMode.POSITION:
                param_ptr = memory[instr_ptr]
            elif mode == ParamMode.IMMEDIATE:
                param_ptr = instr_ptr
            elif mode == ParamMode.RELATIVE:
                param_ptr = relative_ptr + memory[instr_ptr]
        except IndexError:
            pass
        finally:
            param_ptrs.append(param_ptr)
    return op_code, param_ptrs


def run_program_async(program, **kwargs):
    program = list(program)  # Make a copy because we mutate it.
    memory = kwargs.get('memory', program + [0 for _ in range(10000)])
    program_input = kwargs.get('program_input', [])
    program_output = kwargs.get('program_output', [])
    instr_ptr = kwargs.get('instr_ptr', 0)
    relative_ptr = kwargs.get('relative_ptr', 0)

    def state(status):
        return {
            'program': program,
            'program_input': program_input,
            'program_output': program_output,
            'instr_ptr': instr_ptr,
            'status': status,
            'relative_ptr': relative_ptr,
            'memory': memory
        }

    while True:
        if memory[instr_ptr] == OpCode.HALT:
            return state(ProgState.HALTED)

        op_code, param_ptrs = parse_operation(memory, instr_ptr, relative_ptr)

        if op_code == OpCode.ADD:
            memory[param_ptrs[2]] = memory[param_ptrs[0]] + memory[param_ptrs[1]]
            instr_ptr += 4
        elif op_code == OpCode.MULTIPLY:
            memory[param_ptrs[2]] = memory[param_ptrs[0]] * memory[param_ptrs[1]]
            instr_ptr += 4
        elif op_code == OpCode.INPUT:
            if not program_input:
                return state(ProgState.NEEDS_INPUT)
            memory[param_ptrs[0]] = program_input.pop(0)
            instr_ptr += 2
        elif op_code == OpCode.OUTPUT:
            program_output.append(memory[param_ptrs[0]])
            instr_ptr += 2
            return state(ProgState.GENERATED_OUTPUT)
        elif op_code == OpCode.JUMP_IF_TRUE:
            instr_ptr = memory[param_ptrs[1]] if memory[param_ptrs[0]] != 0 else instr_ptr + 3
        elif op_code == OpCode.JUMP_IF_FALSE:
            instr_ptr = memory[param_ptrs[1]] if memory[param_ptrs[0]] == 0 else instr_ptr + 3
        elif op_code == OpCode.LESS_THAN:
            memory[param_ptrs[2]] = 1 if memory[param_ptrs[0]] < memory[param_ptrs[1]] else 0
            instr_ptr += 4
        elif op_code == OpCode.EQUALS:
            memory[param_ptrs[2]] = 1 if memory[param_ptrs[0]] == memory[param_ptrs[1]] else 0
            instr_ptr += 4
        elif op_code == OpCode.ADJUST_RELATIVE_PTR:
            relative_ptr += memory[param_ptrs[0]]
            instr_ptr += 2


def run_program(program, program_input=None):
    program_input = program_input or []
    state = run_program_async(program, program_input=program_input)
    while state['status'] != ProgState.HALTED:
        state = run_program_async(**state)
    return state


if __name__ == '__main__':
    puzzle_input = [int(i) for i in open('day_9.in').read().split(',')]

    # Part 1
    sample_program = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    assert run_program(sample_program)['program_output'] == sample_program
    assert run_program([104, 1125899906842624, 99])['program_output'] == [1125899906842624]
    assert len(str(run_program([1102, 34915192, 34915192, 7, 4, 7, 99, 0])['program_output'][0])) == 16

    print(run_program(puzzle_input, program_input=[1])['program_output'])

    # Part 2
    print(run_program(puzzle_input, program_input=[2])['program_output'])
