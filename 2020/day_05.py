def decode_boarding_pass(bp):
    binary = bp.translate(bp.maketrans('FBLR', '0101'))
    id_ = int(binary, base=2)
    row = id_ >> 3
    col = id_ & int('111', base=2)
    return row, col, id_


if __name__ == '__main__':
    puzzle_input = [line for line in open('day_05.in').read().split('\n')]

    # Part 1
    assert decode_boarding_pass('BFFFBBFRRR') == (70, 7, 567)
    assert decode_boarding_pass('FFFBBBFRRR') == (14, 7, 119)
    assert decode_boarding_pass('BBFFBBFRLL') == (102, 4, 820)
    seats = []
    highest = 0
    for code in puzzle_input:
        _, __, seat_id = decode_boarding_pass(code)
        seats.append(seat_id)
        highest = max(seat_id, highest)
    print(highest)

    # Part 2
    sorted_seats = sorted(seats)
    for i in range(128 * 8):
        if i not in sorted_seats and i - 1 in sorted_seats and i + 1 in sorted_seats:
            print(i)
