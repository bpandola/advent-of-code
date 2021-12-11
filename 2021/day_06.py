def parse_input(filename):
    fish = [int(n) for n in open(filename).read().split(',')]
    return fish


class LanternFish:

    def __init__(self, timer=8, count=1):
        self.timer = timer
        self.prev = None
        self.count = count

    def tick(self):
        self.prev = self.timer
        self.timer -= 1
        if self.timer == -1:
            self.timer = 6

    @property
    def should_spawn(self):
        return self.prev == 0 and self.timer == 6

    @property
    def age(self):
        return self.timer


class Simulation:

    def __init__(self, fish_ages):
        self.fish = []
        for age in fish_ages:
            existing_fish = self.get_fish_by_age(age)
            if existing_fish is None:
                self.fish.append(LanternFish(age))
            else:
                existing_fish.count += 1

    def get_fish_by_age(self, age):
        for f in self.fish:
            if f.age == age:
                return f
        return None

    def tick(self):
        new_fish = 0
        for f in self.fish:
            f.tick()
            if f.should_spawn:
                new_fish += f.count
        if new_fish:
            existing_fish = self.get_fish_by_age(8)
            if existing_fish is None:
                fish = LanternFish()
                fish.count = new_fish
                self.fish.append(fish)
            else:
                existing_fish.count += new_fish


def run_simulation(fish, steps=80):
    simulation = Simulation(fish)
    for i in range(steps):
        simulation.tick()
    return sum([f.count for f in simulation.fish])


if __name__ == '__main__':
    puzzle_input = parse_input('day_06.in')
    sample_input = parse_input('day_06.in.sample_01')

    # Part 1
    assert run_simulation(sample_input) == 5934
    print(run_simulation(puzzle_input))

    # Part 2
    assert run_simulation(sample_input, steps=256) == 26984457539
    print(run_simulation(puzzle_input, steps=256))
