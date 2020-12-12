import math
def parse_input(filename):
    lines = [line.strip() for line in open(filename).read().split('\n')]
    instructions = []
    for line in lines:
        op, value = line[0], int(line[1:])
        instructions.append((op, value))
    return instructions

def calc_manhattan_dist(instructions):
    delta_x = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
    delta_y = {'L': 0, 'R': 0, 'U': 1, 'D': -1}
    robot_to_direction_map = {'^': 'U', 'v': 'D', '<': 'L', '>': 'R', }
    # current_direction = robot_to_direction_map[area_map[robot_pos]]
    x, y = 0,0
    heading = 'R'

    headings_by_turn = {
        'R': {
            'L': {90: 'U', 180: 'R', 270: 'D'},
            'R': {90: 'D', 180: 'L', 270: 'U'},
            'U': {90: 'R', 180: 'D', 270: 'L'},
            'D': {90: 'L', 180: 'U', 270: 'R'},

        },
        'L': {
            'L': {90: 'D', 180: 'R', 270: 'U'},
            'R': {90: 'U', 180: 'L', 270: 'D'},
            'U': {90: 'L', 180: 'D', 270: 'R'},
            'D': {90: 'R', 180: 'U', 270: 'L'},

        }
    }

    for op, value in instructions:
        if op == 'N':
            y+=1*value
        elif op == 'S':
            y-=1*value
        elif op == 'E':
            x+=1*value
        elif op == 'W':
            x-=1*value
        elif op == 'F':
            x+=delta_x[heading]*value
            y+=delta_y[heading]*value
        elif op == 'L' or op == 'R':
            heading = headings_by_turn[op][heading][value]
        else:
            raise RuntimeError('bad op')

    return abs(x) + abs(y)


def calc_waypoint_dist(instructions):
    delta_x = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
    delta_y = {'L': 0, 'R': 0, 'U': -1, 'D': 1}
    robot_to_direction_map = {'^': 'U', 'v': 'D', '<': 'L', '>': 'R', }
    # current_direction = robot_to_direction_map[area_map[robot_pos]]
    x, y = 0,0
    way_x, way_y = 10, 1
    heading = 'R'
    way_headings = ['R','U']

    headings_by_turn = {
        'R': {
            'L': {90: 'U', 180: 'R', 270: 'D'},
            'R': {90: 'D', 180: 'L', 270: 'U'},
            'U': {90: 'R', 180: 'D', 270: 'L'},
            'D': {90: 'L', 180: 'U', 270: 'R'},

        },
        'L': {
            'L': {90: 'D', 180: 'R', 270: 'U'},
            'R': {90: 'U', 180: 'L', 270: 'D'},
            'U': {90: 'L', 180: 'D', 270: 'R'},
            'D': {90: 'R', 180: 'U', 270: 'L'},

        }
    }

    for op, value in instructions:
        if op == 'N':
            way_y+=1*value
        elif op == 'S':
            way_y-=1*value
        elif op == 'E':
            way_x+=1*value
        elif op == 'W':
            way_x-=1*value
        elif op == 'F':
            dx = way_x-x
            dy = way_y-y
            x+=dx*value
            y+=dy*value
            way_x+=dx*value
            way_y+=dy*value
        elif op == 'L' or op == 'R':
            px, py = way_x, way_y
            ox, oy = x, y
            angle = math.radians(-value if op == 'R' else value)
            qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
            qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
            way_x, way_y  = qx, qy
        else:
            raise RuntimeError('bad op')

    return abs(x) + abs(y)
if __name__ == '__main__':
    puzzle_input = parse_input('day_12.in')
    sample_input = parse_input('day_12.in.sample')

    # Part 1
    assert calc_manhattan_dist(sample_input) == 25
    print(calc_manhattan_dist(puzzle_input))

    # Part 1
    assert calc_waypoint_dist(sample_input) == 286
    print(calc_waypoint_dist(puzzle_input))



