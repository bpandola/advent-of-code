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


def map_area(program, display=True):
    # Naive path finding algorithm.  Basically, just follow the right-hand rule
    # and then follow the left-hand rule to map the entire area.
    path_finding_map = [
        [{'W': 'S', 'E': 'N', 'S': 'E', 'N': 'W', }, {'W': 'N', 'E': 'S', 'S': 'W', 'N': 'E', }],
        [{'W': 'N', 'E': 'S', 'S': 'W', 'N': 'E', }, {'W': 'S', 'E': 'N', 'S': 'E', 'N': 'W', }],
    ]
    direction_to_input_code = {'N': 1, 'S': 2, 'W': 3, 'E': 4, }
    delta_x = {'N': 0, 'S': 0, 'W': -1, 'E': 1}
    delta_y = {'N': -1, 'S': 1, 'W': 0, 'E': 0}
    bot_x, bot_y = 0, 0
    direction = 'E'
    area_map = {(bot_x, bot_y): 'X'}
    for path in range(len(path_finding_map)):
        bot_x, bot_y = 0, 0
        state = run_program_async(program)
        while state['status'] != ProgState.HALTED:
            if state['status'] == ProgState.GENERATED_OUTPUT:
                output_code = state['program_output'].pop(0)
                if output_code == 0:
                    # Hit a wall, position unchanged.
                    wall_x = bot_x + delta_x[direction]
                    wall_y = bot_y + delta_y[direction]
                    area_map[(wall_x, wall_y)] = '#'
                    direction = path_finding_map[path][output_code][direction]
                elif output_code in [1, 2]:
                    # Moved one step in requested direction.
                    bot_x += delta_x[direction]
                    bot_y += delta_y[direction]
                    area_map[(bot_x, bot_y)] = '.'
                    # Found oxygen system.
                    if output_code == 2:
                        area_map[(bot_x, bot_y)] = 'O'
                        break
                    direction = path_finding_map[path][output_code][direction]
            elif state['status'] == ProgState.NEEDS_INPUT:
                state['program_input'].append(direction_to_input_code[direction])
            state = run_program_async(**state)
    normalized_data = []
    x_min, x_max = min([x for (x, _) in area_map]), max([x for (x, _) in area_map])
    y_min, y_max = min([y for (y, _) in area_map]), max([y for (y, _) in area_map])
    for j in range(y_min, y_max + 1, 1):
        normalized_data.append([area_map.get((i, j), '?') for i in range(x_min, x_max + 1, 1)])
    if display:
        print_map(normalized_data)
    return normalized_data, (0 - x_min, 0 - y_min), (bot_x - x_min, bot_y - y_min)


def find_shortest_route(start, end, area):
    dead_end = (-1, -1)

    def route_options(pos_cur, pos_prev):
        options = []
        x, y = pos_cur
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            check_x, check_y = x + dx, y + dy
            if area[check_y][check_x] != '#' and (check_x, check_y) != pos_prev:
                options.append((check_x, check_y))
        return options if options else [dead_end]

    routes = [[start]]
    while any(route[-1] not in [end, dead_end] for route in routes):
        for route in routes:
            if route[-1] in [end, dead_end]:
                continue
            possible_next_steps = route_options(route[-1], route[-2] if len(route) > 1 else route[-1])
            for i, position in enumerate(possible_next_steps):
                next_step = position
                if i == 0:
                    route.append(next_step)
                else:
                    fork = route[:-1] + [next_step]
                    routes.append(fork)
    return min([route.index(end) for route in routes if route[-1] == end])


def fill_area_with_oxygen(oxygen_coords, area, display=True):
    step = 0
    spread_points = [oxygen_coords]
    while any(spot for row in area for spot in row if spot == '.'):
        spread_points_new = []
        for x, y in spread_points:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if area[y + dy][x + dx] == '.':
                    area[y + dy][x + dx] = 'O'
                    spread_points_new.append((x + dx, y + dy))
        spread_points = spread_points_new
        step += 1
        if display:
            print_map(area)
            print(step)
    return step


def print_map(map_data):
    for line in range(len(map_data)):
        print(''.join(map_data[line]))


if __name__ == '__main__':
    puzzle_input = [int(i) for i in open('day_15.in').read().split(',')]

    display_mode = False

    # Part 1
    mapped_area, start_coords, o2_coords = map_area(puzzle_input, display=display_mode)
    length = find_shortest_route(start_coords, o2_coords, mapped_area)
    print(length)

    # Part 2
    num_steps = fill_area_with_oxygen(o2_coords, mapped_area, display=display_mode)
    print(num_steps)
