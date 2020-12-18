import ast
def parse_input(filename):
    lines = open(filename).read().split('\n')
    translated = {}
    for y, line in enumerate(lines):
        for x, data in enumerate(lines[y]):
            translated[(x, y, 0, 0)] = data
    return translated

def calculate2(expression):
    ex = [c for c in expression]
    i = 0
    open_parens = []
    close_parens = []
    tokens = []
    operand = None
    left = None
    right = None
    total = 0
    for index, c in enumerate(expression):
        if c == '(':
            open_parens.append(index)
            continue
        elif c == ')':
            close_parens.append(index)
        if len(open_parens) == len(close_parens) and len(open_parens) != 0:
            start = open_parens[0] + 1
            stop = close_parens[-1]
            temp = calculate2(expression[start:stop])
            if left is None:
                left = int(temp)
            else:
                right = int(temp)
            open_parens = []
            close_parens =[]
            if right is None:
                continue
        if len(open_parens) != len(close_parens):
            continue
        if c == ' ':
            continue
        elif c.isdigit():
            if open_parens:
                continue
            if left is None:
                left = int(c)
            else:
                right = int(c)
        elif c in '-+*':
            if left is None:
                continue
            operand = c


        if left is not None and right is not None and operand is not None and not open_parens:
            if operand == '-':
                left = left - right
            elif operand == '+':
                left = left + right
            elif operand == '*':
                left = left * right

            right = operand = None
    return left



def preparse(expression):
    # put parens around all plus signs
    # print(preparse("1 + (2 * 3) + (4 * (5 + 6))"))
    ex = [c for c in expression]
    open_parens = []
    close_parens = []
    index = 0

    def find_index(start, left=True):
        step = -1 if left else 1
        stop = 0 if left else len(ex)
        parens = 0
        for i in range(start, stop, step):
            c = ex[i]
            if c == ')':
                parens-=1
                if not left and not parens:
                    return i
            elif c == '(':
                parens+=1
                if left and not parens:
                    return i
            elif c.isdigit() and not parens:
                return i
        else:
            return i-1 if left else i



    while True:
        c = ex[index]
        # if c == '(':
        #     open_parens.append(index)
        # elif c == ')':
        #     close_parens.append(index)
        if c == '+':
            left = find_index(index, left=True)
            right = find_index(index, left=False)
            ex.insert(left, '(')
            ex.insert(right+2, ')')
            open_parens = close_parens = 0
            index+=1

        index+=1
        if index >= len(ex):
            break

    return ''.join(ex)



def calculate(expression):
    p = ast.parse(expression)
    for node in ast.walk(p):
        print(str(node))



if __name__ == '__main__':
    puzzle_input = [line for line in open('day_18.in').read().split('\n')]
    #sample_input = parse_input('day_18.in.sample')

    assert(calculate2(preparse("1 + 2 * 3 + 4 * 5 + 6"))) == 231
    assert(calculate2(preparse("1 + (2 * 3) + (4 * (5 + 6))"))) == 51
    assert (calculate2(preparse("2 * 3 + (4 * 5)"))) == 46
    assert (calculate2(preparse("5 + (8 * 3 + 9 + 3 * 4 * 3)"))) == 1445
    assert (calculate2(preparse("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))) == 669060

    assert(calculate2(preparse("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))) == 23340

    assert calculate2("1 + 2 * 3 + 4 * 5 + 6") == 71
    print(calculate2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))
    print(sum([calculate2(preparse(exp)) for exp in puzzle_input]))
