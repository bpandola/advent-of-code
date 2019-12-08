def parse_instruction(instruction):
    signal, wire = instruction.split(' -> ')
    num_tokens = len(signal.split(' '))
    if num_tokens == 1:
        left, op, right = signal, None, None
    elif num_tokens == 2:
        op, right = signal.split(' ')
        left = None
    else:
        left, op, right = signal.split(' ')
    return left, op, right, wire


def build_circuit(instructions):
    wires = {}
    for i in instructions:
        left, op, right, out = parse_instruction(i)
        wires[out] = {
            'left': left,
            'op': op,
            'right': right,
        }
    return wires


def run_circuit(instructions, output_wire):
    circuit = build_circuit(list(instructions))  # Make a copy because we mutate it.

    def evaluate(wire_key):
        if wire_key not in circuit:
            return int(wire_key)

        wire = circuit[wire_key]
        op = wire['op']

        if op == 'NOT':
            intermediate = evaluate(wire['right'])
            value = (1 << 16) - 1 - intermediate
        elif op == 'RSHIFT':
            value = evaluate(wire['left']) >> evaluate(wire['right'])
        elif op == 'LSHIFT':
            value = evaluate(wire['left']) << evaluate(wire['right'])
        elif op == 'OR':
            value = evaluate(wire['left']) | evaluate(wire['right'])
        elif op == 'AND':
            value = evaluate(wire['left']) & evaluate(wire['right'])
        elif op is None:
            value = evaluate(wire['left'])
        else:
            raise ValueError('Invalid Operator')

        # Save wire value so we don't have to recurse endlessly...
        circuit[wire_key]['op'] = None
        circuit[wire_key]['left'] = value

        return value

    output = evaluate(output_wire)
    return output


if __name__ == '__main__':
    puzzle_input = open('day_7.in').read().split('\n')

    # Part 1
    example = [
        '123 -> x',
        '456 -> y',
        'x AND y -> d',
        'x OR y -> e',
        'x LSHIFT 2 -> f',
        'y RSHIFT 2 -> g',
        'NOT x -> h',
        'NOT y -> i',
    ]
    assert run_circuit(example, 'd') == 72
    assert run_circuit(example, 'e') == 507
    assert run_circuit(example, 'f') == 492
    assert run_circuit(example, 'g') == 114
    assert run_circuit(example, 'h') == 65412
    assert run_circuit(example, 'i') == 65079
    assert run_circuit(example, 'x') == 123
    assert run_circuit(example, 'y') == 456

    print(run_circuit(puzzle_input, 'a'))

    # Part 2
    puzzle_input = open('day_7.in').read().replace('44430 -> b', '3176 -> b').split('\n')

    print(run_circuit(puzzle_input, 'a'))
