import collections
import math
import collections
Reaction = collections.namedtuple('Reaction', 'chemical quantity ingredients')


def calculate_ore_needed_ref(chemical, amount, graph, consumables=None):
    consumables = consumables if consumables is not None else {}

    while consumables.get(chemical, 0) < amount:

        # Don't have it; have to make it.
        node = graph[chemical]
        for i in node['ingredients']:
            while True:
                if i['chemical'] == 'ORE':
                    consumables['ORE'] = consumables.get('ORE',0) + i['quantity']
                    break
                if i['chemical'] in consumables and consumables[i['chemical']] >= i['quantity']:
                    consumables[i['chemical']] -= i['quantity']
                    break
                calculate_ore_needed_ref(i['chemical'], i['quantity'], graph, consumables)
        consumables[chemical] = consumables.get(chemical, 0) + node['quantity']

    return consumables


def calculate_ore_needed_faster(chemical, amount, graph, consumables=None):
    consumables = consumables if consumables is not None else {}


    available = consumables.get(chemical, 0)
    while available < amount:
        delta = amount - available
        # Don't have it; have to make it.
        node = graph[chemical]
        needed = math.ceil(delta/node['quantity'])
        for i in node['ingredients']:
            while True:
                if i['chemical'] == 'ORE':
                    consumables['ORE'] = consumables.get('ORE',0) + (i['quantity'] * needed)
                    break
                if i['chemical'] in consumables and consumables[i['chemical']] >= (i['quantity'] * needed):
                    consumables[i['chemical']] -= (i['quantity'] * needed)
                    break
                calculate_ore_needed_faster(i['chemical'], (i['quantity']*needed), graph, consumables)
        consumables[chemical] = consumables.get(chemical, 0) + (node['quantity'] * needed)

        available = consumables.get(chemical, 0)
    return consumables


def calculate_ore_needed(chemical, amount, graph):

    result = calculate_ore_needed_faster(chemical, amount, graph)
    return result['ORE']

def calculate_max_fuel(max_ore, graph):
    ore_remaining = max_ore
    fuel_generated = 0

    ore_needed = calculate_ore_needed('FUEL', 1, graph)

    consumables = calculate_ore_needed_faster('FUEL', max_ore/ore_needed, graph)

    #consumables = calculate_ore_needed_faster('FUEL', 2074844, graph)


    while True:

        fuel_generated += consumables.pop('FUEL')
        ore_remaining -= consumables.pop('ORE')

        if sum(consumables.values()) == 0:
            fuel_generated = ((max_ore // (max_ore - ore_remaining)) * fuel_generated)
            ore_remaining = (max_ore % (max_ore - ore_remaining))
        print(ore_remaining)
        if ore_remaining < 0:
            fuel_generated -= 1
            break
        consumables = calculate_ore_needed_faster('FUEL', 1, graph, consumables)


    return fuel_generated

def parse_input2(data):
    reactions = []
    for entity in data:
        chain, output = entity.split('=>')
        output_amt, output_chem, = output.strip().split(' ')
        ingredients = []
        for i in chain.split(','):
            amount, name = i.strip().split(' ')
            r = Reaction(chemical=name, quantity=int(amount), ingredients=[])
            ingredients.append(r)
        reaction = Reaction(chemical=output_chem, quantity=int(output_amt), ingredients=ingredients)
        reactions.append(reaction)
    return reactions


def parse_input(data):
    reactions = parse_input2(data)
    graph = {}

    for r in reactions:
        assert r.chemical not in graph
        graph[r.chemical] = {
            'quantity': r.quantity,
            'ingredients': [{'chemical': i.chemical, 'quantity': i.quantity} for i in r.ingredients]
        }

    return graph


if __name__ == '__main__':
    puzzle_input = open('day_14.in').read().split('\n')

    # Part 1
    sample_1 = [
        '10 ORE => 10 A',
        '1 ORE => 1 B',
        '7 A, 1 B => 1 C',
        '7 A, 1 C => 1 D',
        '7 A, 1 D => 1 E',
        '7 A, 1 E => 1 FUEL',
    ]
    assert calculate_ore_needed('FUEL',1,parse_input(sample_1)) == 31

    sample_2 = [
        '9 ORE => 2 A',
        '8 ORE => 3 B',
        '7 ORE => 5 C',
        '3 A, 4 B => 1 AB',
        '5 B, 7 C => 1 BC',
        '4 C, 1 A => 1 CA',
        '2 AB, 3 BC, 4 CA => 1 FUEL',
    ]
    assert calculate_ore_needed('FUEL', 1,parse_input(sample_2)) == 165

    sample_3 = [
        '157 ORE => 5 NZVS',
        '165 ORE => 6 DCFZ',
        '44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL',
        '12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ',
        '179 ORE => 7 PSHF',
        '177 ORE => 5 HKGWZ',
        '7 DCFZ, 7 PSHF => 2 XJWVT',
        '165 ORE => 2 GPVTF',
        '3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT',
    ]
    assert calculate_ore_needed('FUEL', 1,parse_input(sample_3)) == 13312

    sample_4 = [
        '2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG',
        '17 NVRVD, 3 JNWZP => 8 VPVL',
        '53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL',
        '22 VJHF, 37 MNCFX => 5 FWMGM',
        '139 ORE => 4 NVRVD',
        '144 ORE => 7 JNWZP',
        '5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC',
        '5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV',
        '145 ORE => 6 MNCFX',
        '1 NVRVD => 8 CXFTF',
        '1 VJHF, 6 MNCFX => 4 RFSQX',
        '176 ORE => 6 VJHF',
    ]
    assert calculate_ore_needed('FUEL',1, parse_input(sample_4)) == 180697

    sample_5 = [
        '171 ORE => 8 CNZTR',
        '7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL',
        '114 ORE => 4 BHXH',
        '14 VRPVC => 6 BMBT',
        '6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL',
        '6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT',
        '15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW',
        '13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW',
        '5 BMBT => 4 WPTQ',
        '189 ORE => 9 KTJDG',
        '1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP',
        '12 VRPVC, 27 CNZTR => 2 XDBXC',
        '15 KTJDG, 12 BHXH => 5 XCVML',
        '3 BHXH, 2 VRPVC => 7 MZWV',
        '121 ORE => 7 VRPVC',
        '7 XCVML => 6 RJRHP',
        '5 BHXH, 4 VRPVC => 5 LTCX',
    ]
    assert calculate_ore_needed('FUEL', 1, parse_input(sample_5)) == 2210736

    print(calculate_ore_needed('FUEL',1, parse_input(puzzle_input)))

    # Part 2
    assert calculate_max_fuel(1000000000000, parse_input(sample_3)) == 82892753
    assert calculate_max_fuel(1000000000000, parse_input(sample_4)) == 5586022
    assert calculate_max_fuel(1000000000000, parse_input(sample_5)) == 460664

    print(calculate_max_fuel(1000000000000, parse_input(puzzle_input)))
