def evaluate(expression):
    open_parens = []
    close_parens = []
    left, right, operand = None, None, None
    for index, c in enumerate(expression):
        if c == '(':
            open_parens.append(index)
            continue
        elif c == ')':
            close_parens.append(index)
        if len(open_parens) == len(close_parens) and len(open_parens) != 0:
            start = open_parens[0] + 1
            stop = close_parens[-1]
            temp = evaluate(expression[start:stop])
            if left is None:
                left = int(temp)
            else:
                right = int(temp)
            open_parens = []
            close_parens = []
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

        if (
                left is not None and
                right is not None and
                operand is not None
                and not open_parens
        ):
            if operand == '-':
                left = left - right
            elif operand == '+':
                left = left + right
            elif operand == '*':
                left = left * right

            right = operand = None
    return left


def new_rules(expression):
    # Put parentheses around all plus signs to ensure order of operations.
    ex = [c for c in expression]

    def find_parens(start, is_left_op=True):
        step = -1 if is_left_op else 1
        stop = 0 if is_left_op else len(ex)
        i = parens = 0
        for i in range(start, stop, step):
            c = ex[i]
            if c == ')':
                parens -= 1
                if not is_left_op and not parens:
                    break
            elif c == '(':
                parens += 1
                if is_left_op and not parens:
                    break
            elif c.isdigit() and not parens:
                break
        else:
            i = i - 1 if is_left_op else i
        return i

    index = 0
    while True:
        c = ex[index]
        if c == '+':
            left = find_parens(index, is_left_op=True)
            right = find_parens(index, is_left_op=False)
            ex.insert(left, '(')
            ex.insert(right + 2, ')')  # Have to account for left being added.
            index += 1
        index += 1
        if index >= len(ex):
            break

    return ''.join(ex)


if __name__ == '__main__':
    puzzle_input = [line for line in open('day_18.in').read().split('\n')]

    # Part 1
    def p1(x): return evaluate(x)
    assert p1("1 + 2 * 3 + 4 * 5 + 6") == 71
    assert p1("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert p1("2 * 3 + (4 * 5)") == 26
    assert p1("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
    assert p1("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
    assert p1("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632
    print(sum([p1(exp) for exp in puzzle_input]))

    # Part 2
    def p2(x): return evaluate(new_rules(x))
    assert p2("1 + 2 * 3 + 4 * 5 + 6") == 231
    assert p2("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert p2("2 * 3 + (4 * 5)") == 46
    assert p2("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 1445
    assert p2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 669060
    assert p2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 23340
    print(sum([p2(exp) for exp in puzzle_input]))
