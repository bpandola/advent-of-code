import math
from functools import reduce
def parse_input2(filename):
    lines = [line.strip() for line in open(filename).read().split('\n')]
    timestamp = int(lines[0])
    buses = [int(num) for num in lines[1].split(',') if num != 'x']


    return timestamp, buses

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)
def parse_input3(filename):
    lines = [line.strip() for line in open(filename).read().split('\n')]
    buses = [num for num in lines[1].split(',')]

    nums_only = sorted([int(bus) for bus in buses if bus != 'x'])
    #max_bus = max([int(bus) for bus in buses if bus != 'x'])
    max_bus = nums_only[-1]
    max_bus_index = buses.index(str(max_bus))
    max_bus2 = nums_only[-2]
    max_bus2_index = buses.index(str(max_bus2))
    bleh = lcm(max_bus, max_bus2+max_bus_index-max_bus2_index)

    index = 1
    can_break = False
    start = 0 #100014096222497
    while True:
        timestamp = max_bus*index# bleh*index # +=1 #  = max_bus*index
        departures = []
        for i, bus in enumerate(buses):
            if bus == 'x':
                temp2 = timestamp-max_bus_index+i
                #departures.append(timestamp-max_bus_index+i)
            else:
                temp = timestamp % int(bus)
                temp2 = timestamp - temp
                if temp2 < timestamp-max_bus_index+i:
                    temp2 += int(bus)
            if i:
                if temp2 - departures[i - 1] != 1:
                    print(departures)
                    break
            departures.append(temp2)
        else:
            print(departures)
            can_break = True
        print(departures)



        # can_break = True
        # for j in range(1,len(departures)):
        #     if departures[j] - departures[j-1] != 1:
        #         can_break=False
        #         break

        if can_break:
            break
        index+=1
        #print(timestamp)



    print(departures)
    return departures


def parse_input(filename):
    lines = [line.strip() for line in open(filename).read().split('\n')]
    buses = [num for num in lines[1].split(',')]

    nums_only = sorted([int(bus) for bus in buses if bus != 'x'])
    #max_bus = max([int(bus) for bus in buses if bus != 'x'])
    max_bus = nums_only[-1]
    max_bus_index = buses.index(str(max_bus))
    max_bus2 = nums_only[-2]
    max_bus2_index = buses.index(str(max_bus2))
    bleh = lcm(max_bus, max_bus2+max_bus_index-max_bus2_index)
    number = 1068785 #max_bus
    while True:
        num_1 = 59
        num_2 = 31

        mod_1 = number % num_1

        mod_2 = num_2 - (number % num_2)

        print(number, mod_1, mod_2)


        # magic_number = number%int(buses[0])
        # for index, bus in enumerate(buses):
        #     if bus == 'x':
        #         continue
        #     elif (number%int(bus))+index != magic_number:
        #             break
        # else:
        #     print(number)


        # if (number%7) == (number%13)+1 ==(number % max_bus)+4 == (number % max_bus2)+6:
        #     print(number)
        number-=59
        # if number > 1070000:
        #     break



    index = 1
    can_break = False
    start = number #100014096222497
    while True:
        timestamp = start*index# bleh*index # +=1 #  = max_bus*index
        departures = []
        for i, bus in enumerate(buses):
            if bus == 'x':
                temp2 = timestamp-max_bus_index+i
                #departures.append(timestamp-max_bus_index+i)
            else:
                temp = timestamp % int(bus)
                temp2 = timestamp - temp
                if temp2 < timestamp-max_bus_index+i:
                    temp2 += int(bus)
            # if i:
            #     if temp2 - departures[i - 1] != 1:
            #         print(departures)
            #         break
            departures.append(temp2)
        # else:
        #     print(departures)
        #     can_break = True
        print(departures)



        can_break = True
        for j in range(1,len(departures)):
            if departures[j] - departures[j-1] != 1:
                can_break=False
                break

        if can_break:
            print(index)
            break
        index+=1
        #print(timestamp)



    print(departures)
    return departures

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def parse_input4(filename):
    lines = [line.strip() for line in open(filename).read().split('\n')]
    buses = [num for num in lines[1].split(',')]


    nums_only = [int(bus) for bus in buses if bus != 'x']
    bus_tups = []
    for i, bus in enumerate(nums_only):
        bus_index = buses.index(str(bus))
        value = bus - buses.index(str(bus))
        remainder = value % bus
        tup = (remainder, bus)
        bus_tups.append(tup)

    sum = 0
    prod = reduce(lambda a, b: a * b, nums_only)
    for  a_i,n_i in bus_tups:
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

    #max_bus = max([int(bus) for bus in buses if bus != 'x'])
    max_bus = max(nums_only)
    max_bus_index = buses.index(str(max_bus))
    max_bus2 = nums_only[-2]
    max_bus2_index = buses.index(str(max_bus2))
    bleh = lcm(max_bus, max_bus2+max_bus_index-max_bus2_index)

    index = 1
    can_break = False
    index = 247086664214628 # manually calculated based off highest number
    #         2428868425949 first answer I got online calc
    # I typo the first tuple!!!
    #        14585777533461
    # still too low wtf
    # I fucking forgot a wholetuple!!!
    #       247086664214628
    # THis right!!!
    #index = 1068785 // 59
    while True:
        timestamp = index# bleh*index # +=1 #  = max_bus*index
        departures = []
        for i in range(1, len(bus_tups)):
            remainder, bus = bus_tups[i]
            ts_mod = timestamp % bus
            if ts_mod != remainder:
                break
        else:
            #print(departures)
            can_break = True
        #print(departures)



        # can_break = True
        # for j in range(1,len(departures)):
        #     if departures[j] - departures[j-1] != 1:
        #         can_break=False
        #         break

        if can_break:
            break
        index+=1
        if index % 10000000 == 0:
            print(timestamp)



    print(timestamp)
    return ts_mod
if __name__ == '__main__':
    puzzle_input = parse_input4('day_13.in')
    #sample_input = parse_input4('day_13.in.sample')

    # Part 1
    # timestamp, buses = sample_input
    #
    # departures = []
    # for index, b in enumerate(buses):
    #     temp = timestamp%b
    #     departures.append( b - temp)
    #
    # print(min(departures) * buses[departures.index(min(departures))] )
    #
    #
    #
    #
    # Part 2
    print(puzzle_input)
