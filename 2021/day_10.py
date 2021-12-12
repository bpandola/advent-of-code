def parse_input(filename):
    lines = open(filename).read().split('\n')
    return lines


SCORE_ERROR = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

SCORE_AUTOCOMPLETE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

MATCHERS = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

MATCHERS_AUTOCOMPLETE = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

OPENERS = ['(', '[', '{', '<']


def score_syntax(lines):
    error_score = 0
    autocomplete_scores = []
    for line in lines:
        stack = []
        for c in line:
            if c in OPENERS:
                stack.append(c)
                continue
            if c in MATCHERS.keys():
                if stack[-1] == MATCHERS[c]:
                    stack.pop()
                    continue
                else:
                    # illegal
                    error_score += SCORE_ERROR[c]
                    stack = []
                    break
        # Autocomplete:
        if len(stack):
            completion = [MATCHERS_AUTOCOMPLETE[c] for c in reversed(stack)]
            total = 0
            for c in completion:
                total *= 5
                total += SCORE_AUTOCOMPLETE[c]
            autocomplete_scores.append(total)
    autocomplete_scores = sorted(autocomplete_scores)
    return error_score, autocomplete_scores[len(autocomplete_scores) >> 1]


def syntax_error_score(syntax):
    return score_syntax(syntax)[0]


def autocompletion_score(syntax):
    return score_syntax(syntax)[1]


if __name__ == '__main__':
    puzzle_input = parse_input('day_10.in')
    sample_input = parse_input('day_10.in.sample_01')

    # Part 1
    assert syntax_error_score(sample_input) == 26397
    print(syntax_error_score(puzzle_input))

    # Part 2
    assert autocompletion_score(sample_input) == 288957
    print(autocompletion_score(puzzle_input))
