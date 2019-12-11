from collections import defaultdict


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


def run_hull_painting_robot(program, program_input=None):
    program_input = program_input if program_input is not None else []
    delta_x = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
    delta_y = {'L': 0, 'R': 0, 'U': -1, 'D': 1}
    direction_after_turn = {
        'U': ('L', 'R'),
        'D': ('R', 'L'),
        'L': ('D', 'U'),
        'R': ('U', 'D'),
    }
    # Robot starts at (0,0) facing UP
    x, y = 0, 0
    direction = 'U'
    # All hull panels are currently black (color 0).
    painted_hull = defaultdict(lambda: 0)
    state = run_program_async(program, program_input=program_input)
    while state['status'] != ProgState.HALTED:
        if state['status'] == ProgState.GENERATED_OUTPUT and len(state['program_output']) == 2:
            # First output is color.
            color = state['program_output'].pop(0)
            painted_hull[(x, y)] = color
            # Second is turn direction.
            turn = state['program_output'].pop(0)
            direction = direction_after_turn[direction][turn]
            # After the robot turns, it should always move forward one panel.
            x += delta_x[direction]
            y += delta_y[direction]
        elif state['status'] == ProgState.NEEDS_INPUT:
            # Robot needs current panel color.
            color = painted_hull[(x, y)]
            state['program_input'].append(color)
        state = run_program_async(**state)
    return painted_hull


if __name__ == '__main__':
    puzzle_input = [int(i) for i in open('day_11.in').read().split(',')]

    # Part 1
    panels = run_hull_painting_robot(puzzle_input, [0])
    print(len(panels))

    # Part 2
    hull_panels = run_hull_painting_robot(puzzle_input, [1])
    for j in range(min(y for (_, y) in hull_panels), max(y for (_, y) in hull_panels) + 1, 1):
        row = ''
        for i in range(min(x for (x, _) in hull_panels), max(x for (x, _) in hull_panels) + 1, 1):
            row += '|' if hull_panels[(i, j)] else ' '
        print(row)
