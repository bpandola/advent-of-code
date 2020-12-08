def parse_input(filename):
    lines = [line for line in open(filename).read().split('\n')]
    instructions = []
    for line in lines:
        op, arg = line.split(' ')
        instructions.append((op, int(arg)))
    return instructions


def _run(program, context=None, step_hook=None):
    instructions = list(program)
    context = context or {}
    context['instruction_pointer'] = context.get('instruction_pointer', 0)
    context['accumulator'] = context.get('accumulator', 0)

    while True:
        if step_hook:
            context = step_hook(context)

        if context['instruction_pointer'] >= len(instructions):
            context['halt'] = True

        if context.get('halt', False):
            break

        instruction, argument = instructions[context['instruction_pointer']]

        if instruction == 'nop':
            context['instruction_pointer'] += 1
        elif instruction == 'acc':
            context['accumulator'] += argument
            context['instruction_pointer'] += 1
        elif instruction == 'jmp':
            context['instruction_pointer'] += argument

    return context


def run(program, break_infinite_loop=True):
    seen = []

    def halt_infinite_loop(ctx):
        ip = ctx['instruction_pointer']
        if ip in seen:
            ctx['halt'] = True
        seen.append(ip)
        return ctx

    hook = halt_infinite_loop if break_infinite_loop else None
    context = _run(program, step_hook=hook)
    return context


def get_accumulator_output(program):
    return run(program)['accumulator']


def get_accumulator_after_patching(program):
    for i in range(len(program)):
        program_modified = program[:]
        instruction, argument = program[i]
        if instruction == 'nop':
            instruction = 'jmp'
        elif instruction == 'jmp':
            instruction = 'nop'
        else:
            continue
        program_modified[i] = (instruction, argument)
        context = run(program_modified)
        if context['instruction_pointer'] >= len(program_modified):
            return context['accumulator']
    else:
        raise RuntimeError('No program patches succeeded!')


if __name__ == '__main__':
    puzzle_input = parse_input('day_08.in')
    sample_input = parse_input('day_08.in.sample')

    # Part 1
    assert get_accumulator_output(sample_input) == 5
    print(get_accumulator_output(puzzle_input))

    # Part 2
    assert get_accumulator_after_patching(sample_input) == 8
    print(get_accumulator_after_patching(puzzle_input))
