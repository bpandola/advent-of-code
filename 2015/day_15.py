class Ingredient:

    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavor = int(flavor)
        self.texture = int(texture)
        self.calories = int(calories)


def parse_input(lines):
    ingredients = []
    for line in lines:
        name, attributes = line.split(':')
        attrs = {}
        for attr in attributes.strip().split(','):
            key, value = attr.strip().split(' ')
            attrs[key] = value
        ingredients.append(Ingredient(name, **attrs))
    return ingredients


def generate_permutations_sample(digit_start, digit_end):
    for a in range(digit_start, digit_end + 1):
        for b in range(digit_start, digit_end + 1):
            combination = [a, b]
            if sum(combination) != 100:
                continue
            yield combination


def generate_permutations(digit_start, digit_end):
    for a in range(digit_start, digit_end + 1):
        for b in range(digit_start, digit_end + 1):
            for c in range(digit_start, digit_end + 1):
                for d in range(digit_start, digit_end + 1):
                    combination = [a, b, c, d]
                    if sum(combination) != 100:
                        continue
                    yield combination


def find_highest_scoring_cookie(ingredients, num_teaspoons, gen=generate_permutations, calorie_check=0):
    max_value = 0
    for combination in gen(1, num_teaspoons - 1):
        zeroed = False
        attrs = ['capacity', 'durability', 'flavor', 'texture']
        value = 1
        if calorie_check:
            calories = 0
            for index, ingredient in enumerate(ingredients):
                calories += ingredient.calories * combination[index]
            if calorie_check != calories:
                continue
        for attr in attrs:
            attr_value = 0
            for index, ingredient in enumerate(ingredients):
                attr_value += getattr(ingredient, attr) * combination[index]
            if not attr_value or attr_value < 0:
                zeroed = True
                break
            value *= attr_value
        if zeroed:
            continue
        if value > max_value:
            max_value = value
    return max_value


if __name__ == '__main__':
    puzzle_input = open('day_15.in').read().strip().split('\n')

    # Part 1
    sample_input = [
        "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
        "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3",
    ]
    ingredients = parse_input(sample_input)
    assert find_highest_scoring_cookie(ingredients, 100, generate_permutations_sample) == 62842880

    ingredients = parse_input(puzzle_input)
    print(find_highest_scoring_cookie(ingredients, 100, generate_permutations))

    # Part 2
    ingredients = parse_input(sample_input)
    assert find_highest_scoring_cookie(ingredients, 100, generate_permutations_sample, calorie_check=500) == 57600000

    ingredients = parse_input(puzzle_input)
    print(find_highest_scoring_cookie(ingredients, 100, generate_permutations, calorie_check=500))
