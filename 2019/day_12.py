class Moon:

    def __init__(self, x, y, z, x_vel=0, y_vel=0, z_vel=0):
        self.x = x
        self.y = y
        self.z = z
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.z_vel = z_vel

    def apply_gravity(self, others):
        # It's ok if `self` is in the `others` array; the added velocity will always be 0.
        for other in others:
            self.x_vel += 1 if other.x > self.x else -1 if other.x < self.x else 0
            self.y_vel += 1 if other.y > self.y else -1 if other.y < self.y else 0
            self.z_vel += 1 if other.z > self.z else -1 if other.z < self.z else 0

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.z += self.z_vel

    @property
    def potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    @property
    def kinetic_energy(self):
        return abs(self.x_vel) + abs(self.y_vel) + abs(self.z_vel)

    @property
    def energy(self):
        return self.kinetic_energy * self.potential_energy


def run_simulation(moons, num_steps=1):
    simulation = moons[:]
    for i in range(num_steps):
        for moon in simulation:
            moon.apply_gravity(simulation)
        for moon in simulation:
            moon.move()
    return simulation


def find_simulation_period(moons):
    simulation = moons[:]
    axes = ['x', 'y', 'z']
    axes_starts = [[getattr(m, attr) for m in simulation] for attr in axes]
    axes_periods = [0, 0, 0]
    step = 0
    while True:
        step += 1
        simulation = run_simulation(simulation, num_steps=1)
        for i, axis in enumerate(axes):
            if not axes_periods[i]:
                if [getattr(m, axis) for m in simulation] == axes_starts[i]:
                    axes_periods[i] = step + 1
        if all(period > 0 for period in axes_periods):
            break
    lcd = 1
    for period in axes_periods:
        lcd = least_common_multiple(lcd, period)
    return lcd


def least_common_multiple(a, b):
    from math import gcd
    return a * b // gcd(a, b)


def parse_input(data):
    moons = []
    for entity in data:
        entity = entity.replace('<', '')
        entity = entity.replace('>', '')
        entity = entity.replace(',', '')
        tokens = entity.split(' ')
        x = int(tokens[0].split('=')[-1])
        y = int(tokens[1].split('=')[-1])
        z = int(tokens[2].split('=')[-1])
        moons.append(Moon(x, y, z))
    return moons


if __name__ == '__main__':
    puzzle_input = open('day_12.in').read().split('\n')

    # Part 1
    sample_1 = [
        '<x=-1, y=0, z=2>',
        '<x=2, y=-10, z=-7>',
        '<x=4, y=-8, z=8>',
        '<x=3, y=5, z=-1>',
    ]
    result = run_simulation(parse_input(sample_1), num_steps=10)
    assert sum(moon.energy for moon in result) == 179

    sample_2 = [
        '<x=-8, y=-10, z=0>',
        '<x=5, y=5, z=10>',
        '<x=2, y=-7, z=3>',
        '<x=9, y=-8, z=-3>',
    ]
    result = run_simulation(parse_input(sample_2), num_steps=100)
    assert sum(moon.energy for moon in result) == 1940

    result = run_simulation(parse_input(puzzle_input), num_steps=1000)
    print(sum(moon.energy for moon in result))

    # Part 2
    assert find_simulation_period(parse_input(sample_1)) == 2772
    assert find_simulation_period(parse_input(sample_2)) == 4686774924

    print(find_simulation_period(parse_input(puzzle_input)))
