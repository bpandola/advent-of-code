import re

HYPERNET_REGEX = re.compile(r'\[(.*?)\]')


def parse_ip_address(address):
    hypernet_sequences = HYPERNET_REGEX.findall(address)
    for sequence in hypernet_sequences:
        address = address.replace('[' + sequence + ']', ',')
    supernet_sequences = address.split(',')
    return supernet_sequences, hypernet_sequences


def contains_abba(sequence):
    for i in range(len(sequence) - 3):
        if sequence[i] == sequence[i + 3]:
            if sequence[i + 1] == sequence[i + 2]:
                if sequence[i] != sequence[i + 1]:
                    return True
    return False


def find_abas(sequences):
    for sequence in sequences:
        for i in range(len(sequence) - 2):
            if sequence[i] == sequence[i + 2]:
                if sequence[i] != sequence[i + 1]:
                    yield ''.join(sequence[i:i + 3])


def supports_tls(address):
    supernet_sequences, hypernet_sequences = parse_ip_address(address)
    return any([contains_abba(ip) for ip in supernet_sequences]) and \
        not any(contains_abba(seq) for seq in hypernet_sequences)


def supports_ssl(address):
    supernet_sequences, hypernet_sequences = parse_ip_address(address)
    for aba in find_abas(supernet_sequences):
        bab = aba[1:2] + aba[0:1] + aba[1:2]
        for sequence in hypernet_sequences:
            if bab in sequence:
                return True
    return False


if __name__ == '__main__':
    puzzle_input = open('day_07.in').read().split('\n')

    # Part 1
    sample_input_1 = [
        'abba[mnop]qrst',
        'abcd[bddb]xyyx',
        'aaaa[qwer]tyui',
        'ioxxoj[asdfgh]zxcvbn',
    ]
    assert supports_tls(sample_input_1[0]) is True
    assert supports_tls(sample_input_1[1]) is False
    assert supports_tls(sample_input_1[2]) is False
    assert supports_tls(sample_input_1[3]) is True

    print(len([ip for ip in puzzle_input if supports_tls(ip)]))

    # Part 2
    sample_input_2 = [
        'aba[bab]xyz',
        'xyx[xyx]xyx',
        'aaa[kek]eke',
        'zazbz[bzb]cdb',
    ]
    assert supports_ssl(sample_input_2[0]) is True
    assert supports_ssl(sample_input_2[1]) is False
    assert supports_ssl(sample_input_2[2]) is True
    assert supports_ssl(sample_input_2[3]) is True

    print(len([ip for ip in puzzle_input if supports_ssl(ip)]))
