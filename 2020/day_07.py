from functools import reduce


def parse_input(filename):
    lines = [line for line in open(filename).read().split('\n')]
    bags = {}
    for line in lines:
        outer, contents = line.split(' bags contain')
        outer = outer.strip()
        contents = contents.split(',')
        bags[outer] = {}
        for bag in contents:
            content = bag.split(' ')
            if content[1] == 'no':
                continue
            bag_name = content[2] + ' ' + content[3]
            bags[outer][bag_name] = int(content[1])
    return bags


def find_bags_that_contain_color(bag_color_to_find, bags):
    contains_color = set()

    def traverse(bag_color, path):
        for b in bags[bag_color]:
            temp_path = traverse(b, path + [b])
            if temp_path[-1] == bag_color_to_find:
                for i in range(len(temp_path) - 1):
                    contains_color.add(temp_path[i])
        return path

    for bag in bags:
        traverse(bag, [bag])
    return contains_color


def bagception(container_bag, bags):
    # Count all the bags within the bags... within the container bag.
    bag_counts = []

    def traverse(bag_color, path):
        for b in bags[bag_color]:
            temp_path = traverse(b, path + [b] + [bags[bag_color][b]])
            # Avert thy gaze!!!
            # Basically, our path is bag color and counts:
            # Example: ['shiny gold', 'dark olive', 1, 'faded blue', 3]
            # So we step by 2 and drop the first item to get just the counts...
            # Obviously, there must be a better way.  But this works!
            bag_counts.append(temp_path[::2][1:])
        return path

    traverse(container_bag, [container_bag])
    total_bags = 0
    for counts  in bag_counts:
        sub_total = reduce(lambda x, y: x * y, counts)
        total_bags += sub_total
    return total_bags


if __name__ == '__main__':
    puzzle_input = parse_input('day_07.in')

    # Part 1
    sample_input = parse_input('day_07.in.sample_01')
    assert len(find_bags_that_contain_color('shiny gold', sample_input)) == 4
    print(len(find_bags_that_contain_color('shiny gold', puzzle_input)))

    # Part 2
    assert bagception('shiny gold', sample_input) == 32
    sample_input = parse_input('day_07.in.sample_02')
    assert bagception('shiny gold', sample_input) == 126
    print(bagception('shiny gold', puzzle_input))
