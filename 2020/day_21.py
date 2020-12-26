import re


class Food:

    def __init__(self, allergens, ingredients):
        self.allergens = allergens
        self.ingredients = ingredients


def parse_input(filename):
    lines = open(filename).read().split('\n')
    foods = []
    for line in lines:
        match = re.search(r'(?P<ingredients>.*)\(contains (?P<allergens>.*?)\)$', line)
        allergens = match.group('allergens').split(', ')
        ingredients = match.group('ingredients').split()
        food = Food(allergens, ingredients)
        foods.append(food)
    return foods


def determine_which_ingredient_contains_which_allergen(foods):
    # New allergen?   Add all ingredients as possibilities.
    # Seen allergen?  Possible ingredients is intersection of new/existing ingredient lists.
    possibilities = {}
    for food in foods:
        for allergen in food.allergens:
            if allergen not in possibilities:
                possibilities[allergen] = set(food.ingredients)
            else:
                possibilities[allergen] &= set(food.ingredients)
    # Start with any 1-to-1 mappings and whittle down until all are determined.
    determined = {}
    while possibilities:
        known_allergen, known_ingredient = next(
            (k, list(v)[0]) for k, v in possibilities.items() if len(v) == 1
        )
        determined[known_allergen] = known_ingredient
        del possibilities[known_allergen]
        for allergen in possibilities:
            possibilities[allergen].discard(known_ingredient)
    return determined


def count_inert_ingredients(foods, allergen_to_ingredient_mapping):
    total = sum(
        [
            len([
                ingredient for ingredient in food.ingredients
                if ingredient not in allergen_to_ingredient_mapping.values()
            ])
            for food in foods
        ]
    )
    return total


def calc_canonical_dangerous_ingredient_list(allergen_to_ingredient_mapping):
    return ','.join(
        [
            allergen_to_ingredient_mapping[allergen]
            for allergen in sorted(list(allergen_to_ingredient_mapping.keys()))
        ]
    )


if __name__ == '__main__':
    puzzle_input = parse_input('day_21.in')
    sample_input = parse_input('day_21.in.sample')

    # Part 1
    sample_allergens_to_ingredients = determine_which_ingredient_contains_which_allergen(sample_input)
    assert count_inert_ingredients(sample_input, sample_allergens_to_ingredients) == 5

    allergens_to_ingredients = determine_which_ingredient_contains_which_allergen(puzzle_input)
    print(count_inert_ingredients(puzzle_input, allergens_to_ingredients))

    # Part 2
    expected = 'mxmxvkd,sqjhc,fvjkl'
    assert calc_canonical_dangerous_ingredient_list(sample_allergens_to_ingredients) == expected

    print(calc_canonical_dangerous_ingredient_list(allergens_to_ingredients))
