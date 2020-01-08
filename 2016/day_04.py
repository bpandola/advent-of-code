import re

ROOM_REGEX = re.compile(r'(?P<encrypted_name>[A-Za-z-]+)(?P<sector_id>[0-9]+)\[(?P<checksum>[A-Za-z]+)\]')


def parse_encoded_room_name(encoded_name):
    m = ROOM_REGEX.search(encoded_name)
    parsed = dict(m.groupdict())
    parsed['sector_id'] = int(parsed['sector_id'])
    parsed['encoded_name'] = encoded_name
    return parsed


def calculate_checksum(encrypted_name):
    chr_counts = {}
    for c in encrypted_name:
        if c != '-':
            chr_counts[c] = chr_counts.get(c, 0) + 1
    s = {k: v for k, v in sorted(chr_counts.items(), key=lambda item: item[1], reverse=True)}
    most = 10000
    checksum = ''
    tied = ''
    for char, count in s.items():
        if count == most:
            tied = tied + char
        else:
            checksum += ''.join(sorted(tied))
            tied = char
            most = count
    checksum += ''.join(sorted(tied))
    return checksum[:5]


def is_room_real(encoded_room_name):
    parsed_room = parse_encoded_room_name(encoded_room_name)
    return parsed_room['checksum'] == calculate_checksum(parsed_room['encrypted_name'])


def decrypt_room_name(encrypted_name, sector_id):
    decrypted = ''
    for c in encrypted_name:
        if c == '-':
            decrypted += ' '
        else:
            decrypted += chr(((ord(c) - ord('a') + sector_id) % 26) + ord('a'))
    return decrypted.strip()


if __name__ == '__main__':
    puzzle_input = open('day_04.in').read().split('\n')

    # Part 1
    example_rooms = [
        'aaaaa-bbb-z-y-x-123[abxyz]',
        'a-b-c-d-e-f-g-h-987[abcde]',
        'not-a-real-room-404[oarel]',
        'totally-real-room-200[decoy]',
    ]
    assert is_room_real(example_rooms[0]) is True
    assert is_room_real(example_rooms[1]) is True
    assert is_room_real(example_rooms[2]) is True
    assert is_room_real(example_rooms[3]) is False

    assert sum([parse_encoded_room_name(i)['sector_id'] for i in example_rooms if is_room_real(i)]) == 1514

    print(sum([parse_encoded_room_name(i)['sector_id'] for i in puzzle_input if is_room_real(i)]))

    # Part 2
    assert decrypt_room_name('qzmt-zixmtkozy-ivhz-', 343) == 'very encrypted name'

    for i in puzzle_input:
        if is_room_real(i):
            room = parse_encoded_room_name(i)
            decrypted_room_name = decrypt_room_name(room['encrypted_name'], room['sector_id'])
            if decrypted_room_name == 'northpole object storage':
                print(room['sector_id'])
                break
