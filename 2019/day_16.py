

def get_multiplier(digit_index, op_index):
    base_pattern = [0, 1, 0, -1]

    counter = 0
    while True:
        for j in base_pattern:
            for i in range(digit_index+1):
                if counter == op_index + 1:
                    return j
                counter = counter + 1


def get_multipliers(digit_index, num_digits):
    base_pattern = [0, 1, 0, -1]
    phase = []
    counter = 0
    done = False
    while not done:

        for j in base_pattern:
            if done:
                break
            for i in range(digit_index+1):

                phase.append(j)
                counter = counter + 1
                if counter == num_digits + 1:
                    done = True
                    break
    return phase[1:]

def fft(numbers):
    new_number = ''
    number_length = len(str(numbers))
    for j in range(number_length):
        #print('\n')
        value = 0
        multipliers = get_multipliers(j, number_length)
        for index, n in enumerate(str(numbers)):
            value += int(n) * multipliers[index] # get_multiplier(int(j), int(index))
            # print('{}*{} '.format(n, get_multiplier(int(j), int(index))), end='')
        new_number += str(abs(value)%10)
    return new_number

def calc(number, phases):
    new_number = str(number)
    print(new_number[:40])
    for i in range(phases):
        new_number = fft(new_number)
        print(new_number[:40])
    return new_number

def fft2(numbers, repeat=1):
    base_pattern = [0, 1, 0, -1]
    new_number = ''
    number_length = len(str(numbers))
    for j in range(number_length):

        value = 0

        for index, n in enumerate(str(numbers)):
            pattern = base_pattern[((index+1)//(j+1))%4]
            if pattern:
                value += int(n) * pattern # base_pattern[((index+1)//(j+1))%4]
        #print(j, value, str(abs(value)%10))
        new_number += str(abs(value)%10)
    return new_number

def fft3(numbers):
    base_pattern = [0, 1, 0, -1]
    new_number = ''
    number_length = len(str(numbers))
    for j in range(number_length):
        #print(j)
        # pat = []
        # for index, n in enumerate(str(numbers)):
        #     pat.append(base_pattern[((index+1)//(j+1))%4])
        # print(pat)

        value = 0

        for index, n in enumerate(str(numbers)[j:]):

            pattern = base_pattern[((index+j+1)//(j+1))%4]
            #print(pattern)
            if pattern:
                if pattern < 0:
                    value -= int(n)
                else:
                    value += int(n)

        #print(j, str(numbers)[j:j+1], value, str(abs(value)%10))
        new_number += str(abs(value)%10)
    return new_number


def calc2(number, phases, repeat=1):
    new_number = str(number)
    #print(new_number[:80])
    for i in range(phases):
        new_number = fft3(new_number)
        print(new_number[:80])
    return new_number

def show_pattern(number_length):
    base_pattern = [0, 1, 0, -1]
    for j in range(number_length):
        pat = []
        for index in range(number_length):
            pat.append(base_pattern[((index+1)//(j+1))%4])
        print(pat)
if __name__ == '__main__':
    puzzle_input = open('day_16.in').read().strip()
    #print(len(puzzle_input))
    #print(get_multipliers(1, 8))

    # print(calc(12345678, 4))
    #print(calc2(12345678, 4))
    #
    # print(calc(1234567812345678, 4))

    for i in range(24):
        print(i)
        show_pattern(i)

    print(calc2(123456781234567812345678, 4))

    print(calc2(5243213352432133524321335243213352432133, 4))
    # print(calc(77777777, 100))
    #
    # #for i in range(5):
    # #print(get_multiplier(1, 3))
    #
    #print(calc(80871224585914546619083218645595, 100))
    #

    # Part 1
    assert int(calc2(80871224585914546619083218645595, 100)[:8]) == 24176176
    assert int(calc2(19617804207202209144916044189917, 100)[:8]) == 73745418
    assert int(calc2(69317163492948606335995924319873, 100)[:8]) == 52432133

    print(int(calc2(puzzle_input, 100)[:8]))

    # Part 2
    huge_input =puzzle_input
    for i in range(5):
        huge_input += puzzle_input

    #huge_input = huge_input[:int(str(puzzle_input)[:8])+8]
    #print(calc2(puzzle_input, 100))
    #print(calc2(huge_input, 100))
    # print(calc(huge_input, 10))
    #print(calc2(huge_input, 10))