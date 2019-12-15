
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


def play_game(program):
    delta_x = {'N': 0, 'S': 0, 'W': -1, 'E': 1}
    delta_y = {'N': -1, 'S': 1, 'W': 0, 'E': 0}
    direction_map = {
        1: 'N',
        2: 'S',
        3: 'W',
        4: 'E',

        'N':1,
        'S':2,
        'W':3,
        'E':4,
    }
    always_right_non_blocked = {
        'W': 'N',
        'E': 'S',
        'S': 'W',
        'N': 'E',
    }
    always_right_blocked = {
        'W': 'S',
        'E': 'N',
        'S': 'E',
        'N': 'W',
    }
    screen = {}
    score = 0
    bot_x, bot_y= 0,0
    loc_x, loc_y = -1,-1
    steps = [(bot_x, bot_y)]
    dir_cur = 'E'  # Start going right
    tries = [
        [always_right_non_blocked, always_right_blocked],
        [always_right_blocked, always_right_non_blocked],
    ]
    for i in range(2):
        bot_x, bot_y = 0, 0
        state = run_program_async(program)
        while state['status'] != ProgState.HALTED:
            if state['status'] == ProgState.GENERATED_OUTPUT:
                output = state['program_output'].pop(0)
                if output == 0:
                    # Hit a wall, position unchanged.
                    x =bot_x + delta_x[dir_cur]
                    y = bot_y + delta_y[dir_cur]
                    screen[(x, y)] = '#'
                    dir_cur = tries[i][0][dir_cur]
                elif output == 1 or output == 2:
                    # Moved one step in requested direction

                    bot_x  += delta_x[dir_cur]
                    bot_y += delta_y[dir_cur]
                    screen[(bot_x, bot_y)] = '.'
                    if (bot_x, bot_y) in steps:
                        #screen[(bot_x, bot_y)] = ' '
                        steps.pop(steps.index((bot_x, bot_y)))
                    steps.append((bot_x, bot_y))

                    # Try to stay right
                    dir_cur = tries[i][1][dir_cur]
                    if output == 2:
                        # At location of oxygen system
                        screen[(bot_x, bot_y)] = 'X'
                        screen[(0,0)] = '*'
                        loc_x, loc_y = bot_x, bot_y
                        break

                    print(bot_x, bot_y)
            elif state['status'] == ProgState.NEEDS_INPUT:
                state['program_input'].append(direction_map[dir_cur])

            state = run_program_async(**state)
    for j in range(-25, 25, 1):
        line = ''
        for i in range(-25, 25, 1):
            line += str(screen.get((i,j), '?'))
        print(line)

    print(steps[-1])
    routes = [[(0,0)]]

    def find_choices(x,y, x_prev, y_prev):
        choices = []
        valid = ['.','*','X']
        possible_dir = ['N','S','E','W']
        filtered_dir = possible_dir[:]
        if x < x_prev:
            filtered_dir.remove('E')
        if x > x_prev:
            filtered_dir.remove('W')
        if y < y_prev:
            filtered_dir.remove('S')
        if y > y_prev:
            filtered_dir.remove('N')

        for d in filtered_dir:
            check_x, check_y = x + delta_x[d], y + delta_y[d]
            if screen.get((check_x,check_y), None) in valid:
                choices.append(d)
        return choices

    while any(route[-1] not in [(loc_x, loc_y), (-100, -100) ]for route in routes):

        for route in routes:
            (x, y) = route[-1]
            (x_prev, y_prev) = route[-2] if len(route) > 1 else (x, y)
            if (x, y) == (loc_x, loc_y):
                continue
            direction_choices = find_choices(x, y, x_prev, y_prev)
            if not direction_choices and route[-1] != (-100, -100):
                route.append((-100, -100))
                continue
            for i, dir in enumerate(find_choices(x, y, x_prev, y_prev)):
                next_step = (x + delta_x[dir], y+ delta_y[dir])
                if i == 0:
                    route.append(next_step)
                else:
                    fork = route[:-1] + [next_step]
                    routes.append(fork)



    min_length = [route for route in routes if route[-1] == (loc_x,loc_y)]
    print(len(min_length[0])-1)

    data = []
    for j in range(min(y for (_, y) in screen), max(y for (_, y) in screen) + 1, 1):
        for i in range(min(x for (x, _) in screen), max(x for (x, _) in screen) + 1, 1):
            c = screen.get((i, j), '#')
            c = '.' if c == '*' else 'O' if c == 'X' else c
            data.append(c)
    grid_length = 41
    def pr_map(data, grid_length):
        for i in range(grid_length):
            print(''.join(data[i*grid_length:i*grid_length+grid_length]))
    def do_spread(points, data):
        new_spread_points = []
        data = data[:]
        def non_wall(x, y):
            grid_length = 41
            index = y*grid_length+x
            if data[index:index+1] == ['.']:
                data[index:index+1] = 'O'
                new_spread_points.append((x, y))

        for (x, y) in points:
            non_wall(x-1,y)
            non_wall(x+1,y)
            non_wall(x, y-1)
            non_wall(x, y+1)
        return new_spread_points, data

    # Find our starting oxygen.
    y,x  = divmod(data.index('O'), grid_length)
    spread_points = [(x,y)]
    steps = 0
    while True:
        try:
            data.index('.')
        except ValueError:
            # No more no oxygen
            break
        spread_points, data = do_spread(spread_points, data)


        steps += 1
        pr_map(data, grid_length)
        print(steps)
    return screen


if __name__ == '__main__':
    puzzle_input = [int(i) for i in open('day_15.in').read().split(',')]

    # Part 1
    game_screen = play_game(puzzle_input)

