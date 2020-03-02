import re
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


def run_program(program, program_input=None):
    program_input = program_input or []
    state = run_program_async(program, program_input=program_input)
    while state['status'] != ProgState.HALTED:
        state = run_program_async(**state)
    return state


def map_area(program, display=False):
    output = run_program(program)['program_output']
    area = []
    line = []
    for i in output:
        if i == 10:
            if line:
                area.append(line)
                line = []
        else:
            line.append(chr(i))

    if display:
        for line in area:
            print(''.join(line))

    # Translate into a more convenient data structure.
    # defaultdict[(x, y)] = data; default is '.'
    translated = defaultdict(lambda: '.')
    robot_coords = (0, 0)
    for y, line in enumerate(area):
        for x, data in enumerate(area[y]):
            if data == '#':
                translated[(x, y)] = data
            elif data in ['^', 'v', '<', '>']:
                translated[(x, y)] = data
                robot_coords = (x, y)
    return translated, robot_coords


def find_scaffold_intersections(area_map, display=False):
    area = area_map.copy()

    def is_intersection(x, y):
        if area[(x, y)] != '#':
            return False
        if area[(x - 1, y)] != '#':
            return False
        if area[(x + 1, y)] != '#':
            return False
        if area[(x, y - 1)] != '#':
            return False
        if area[(x, y + 1)] != '#':
            return False
        return True

    alignment_sum = 0
    for coords in list(area.keys()):
        if is_intersection(*coords):
            area[coords] = 'O'
            alignment_sum += coords[0] * coords[1]

    if display:
        print_map(area)

    return alignment_sum


def print_map(area_map):
    x_min, x_max = min(x for (x, _) in area_map), max(x for (x, _) in area_map)
    y_min, y_max = min(y for (_, y) in area_map), max(y for (_, y) in area_map)
    for j in range(y_min, y_max + 1, 1):
        row = ''
        for i in range(x_min, x_max + 1, 1):
            row += area_map[(i, j)]
        print(row)


def get_scaffold_path(area_map, robot_pos):
    delta_x = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
    delta_y = {'L': 0, 'R': 0, 'U': -1, 'D': 1}
    robot_to_direction_map = {'^': 'U', 'v': 'D', '<': 'L', '>': 'R', }
    current_direction = robot_to_direction_map[area_map[robot_pos]]
    x, y = robot_pos

    def find_turn():
        direction_to_turn = {
            'U': {'L': 'L', 'R': 'R'},
            'D': {'L': 'R', 'R': 'L'},
            'L': {'D': 'L', 'U': 'R'},
            'R': {'U': 'L', 'D': 'R'},
        }
        opposite_direction = {
            'U': 'D',
            'D': 'U',
            'L': 'R',
            'R': 'L',
        }
        turn_direction = None
        for heading in ['L', 'R', 'D', 'U']:
            if heading in [current_direction, opposite_direction[current_direction]]:
                continue
            if area_map[(x + delta_x[heading], y + delta_y[heading])] == '#':
                turn_direction = direction_to_turn[current_direction][heading]
                break
        return turn_direction, heading

    instructions = []
    index = 0
    while True:
        if area_map[(x + delta_x[current_direction], y + delta_y[current_direction])] != '#':
            # We are blocked.
            turn, current_direction = find_turn()
            if index:
                instructions.append(index)
            if turn is None:
                break
            instructions.append(turn)
            index = 0
        else:
            x += delta_x[current_direction]
            y += delta_y[current_direction]
            index += 1
    return instructions


def compress_path(instructions):
    path = ''.join([str(i) for i in instructions])
    sequence_markers = 'ABCDEF'
    sequences = []
    sequence_start, sequence_end = 0, 0
    while any([c not in sequence_markers for c in path]):
        if path[sequence_start] in sequence_markers:
            sequence_start += 1
            sequence_end += 1
            continue
        elif path[sequence_end] in sequence_markers:
            sequence_end += 1
        elif path[sequence_start:sequence_end] in path[sequence_end:]:
            sequence_end += 1
            continue
        sequences.append(path[sequence_start:sequence_end-1])
        path = path.replace(sequences[-1], sequence_markers[len(sequences)-1])
        sequence_start = sequence_end = 0
    # Translate our compressed path into the expected format.
    move = re.compile('([LR])([0-9]+)')
    movement_routine = ','.join(path)
    movement_functions = [','.join([f'{m[0]},{m[1]}' for m in move.findall(s)]) for s in sequences]
    return movement_routine, movement_functions


if __name__ == '__main__':
    puzzle_input = [int(i) for i in open('day_17.in').read().split(',')]

    display_mode = True

    scaffold_map, robot_position = map_area(puzzle_input, display_mode)

    # Part 1
    print(find_scaffold_intersections(scaffold_map, display_mode))

    # Part 2
    route = get_scaffold_path(scaffold_map, robot_position)
    compressed_path, segments = compress_path(route)
    path_functions = '\n'.join(segments)
    vacuum_program = puzzle_input[:]
    vacuum_program[0] = 2
    video_feed = 'n'  # y or n
    robot_input = f'{compressed_path}\n{path_functions}\n{video_feed}\n'
    robot_input = [ord(c) for c in robot_input]
    print(run_program(vacuum_program, robot_input)['program_output'][-1])
