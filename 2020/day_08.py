

lines = [line for line in open('day_08.in').read().split('\n')]

instructions = []
for line in lines:
    op, arg = line.split(' ')
    arg = int(arg)
    instructions.append((op, arg))

for i in range(len(instructions)):
    accumulator = 0
    inp = 0
    seen = []
    while True:
        if inp in seen:
            break
        if inp >= len(instructions):
            print(accumulator)
            exit()

        seen.append(inp)
        instruction, argument = instructions[inp]
        if inp == i:
            if instruction == 'nop':
                instruction = 'jmp'
            elif instruction == 'jmp':
                instruction = 'nop'
        if instruction == 'nop':
            inp+=1
        elif instruction == 'acc':
            accumulator += argument
            inp += 1
        elif instruction == 'jmp':
            inp+=argument

#print(accumulator)





