import re
from collections import defaultdict
class Food:

    def __init__(self, ingredients, allergens):
        self.ingredients =ingredients
        self.allergens = allergens


def parse_input(filename):
    lines = open(filename).read().split('\n')
    foods = []
    for line in lines:
        match = re.search('(?P<ingredients>.*)\(contains (?P<allergens>.*?)\)$', line)
        ingredients = match.group('ingredients').split()
        allergens = match.group('allergens').split(', ')
        food = Food(ingredients, allergens)
        foods.append(food)
    return foods

if __name__ == '__main__':
    puzzle_input = parse_input('day_21.in')
    sample_input = parse_input('day_21.in.sample')
    my_input =  puzzle_input
    # New allergen?  Add all ingredients to possibility
    # Seen allergen?  Possiblity is only if in existing possibilities and new list set &
    a_to_i = {}
    for food in my_input:
        for a in food.allergens:
            if a not in a_to_i:
                a_to_i[a] = set(food.ingredients)
            else:
                a_to_i[a] &= set(food.ingredients)
    total_ingredients_that_could_contain_allergen = set()
    for allegen, ingredients in a_to_i.items():
        total_ingredients_that_could_contain_allergen |= ingredients
    total_no_allergens = 0
    for food in my_input:
        for ingredient in food.ingredients:
            if ingredient not in total_ingredients_that_could_contain_allergen:
                total_no_allergens+=1
    print(total_no_allergens)
    finalized = {}
    while a_to_i:

        known_allergen, known_ingredient = next((k,list(v)[0]) for k,v in a_to_i.items() if len(v)==1)
        finalized[known_allergen] = known_ingredient
        del a_to_i[known_allergen]
        for key, value in a_to_i.items():
            a_to_i[key].discard(known_ingredient)
    canonical_dangerous = ''
    for allergen in sorted(list(finalized.keys())):
        canonical_dangerous += f"{finalized[allergen]},"


    print(canonical_dangerous[:-1])