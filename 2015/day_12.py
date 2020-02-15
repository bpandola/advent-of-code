import json


def find_sum(obj, current_sum=0, ignore_obj_value=None):
    if isinstance(obj, list):
        for item in obj:
            current_sum = find_sum(item, current_sum, ignore_obj_value)
    elif isinstance(obj, dict):
        if ignore_obj_value is None or ignore_obj_value not in obj.values():
            for item in obj.values():
                current_sum = find_sum(item, current_sum, ignore_obj_value)
    elif isinstance(obj, int):
        current_sum += obj
    return current_sum


if __name__ == '__main__':
    puzzle_input = json.loads(open('day_12.in').read().strip())

    # Part 1
    assert find_sum([1, 2, 3]) == find_sum({"a": 2, "b": 4}) == 6
    assert find_sum([[[3]]]) == find_sum({"a": {"b": 4}, "c": -1}) == 3
    assert find_sum({"a": [-1, 1]}) == find_sum([-1, {"a": 1}]) == 0
    assert find_sum([]) == find_sum({}) == 0

    print(find_sum(puzzle_input))

    # Part 2
    IGNORED = 'red'
    assert find_sum([1, 2, 3], ignore_obj_value=IGNORED) == 6
    assert find_sum([1, {"c": "red", "b": 2}, 3], ignore_obj_value=IGNORED) == 4
    assert find_sum({"d": "red", "e": [1, 2, 3, 4], "f": 5}, ignore_obj_value=IGNORED) == 0
    assert find_sum([1, "red", 5], ignore_obj_value=IGNORED) == 6

    print(find_sum(puzzle_input, ignore_obj_value=IGNORED))
