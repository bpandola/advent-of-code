lines = [line for line in open('day_05.in').read().split('\n')]


#lines = ['FBFBBFFRLR']
cabin =  {}
highest = 0
for code in lines:

    row, col = 0, 0
    left, right = (0, 127)
    index = 0
    while True:
        c = code[index]
        if c == 'F':
            right = right - ((right - left + 1) // 2)
        elif c == 'B':
            left = left + ((right - left + 1) // 2)
        if left == right:
            row = right
            break
        index += 1
    left, right = 0, 7
    while True:
        c = code[index]
        if c == 'L':
            right = right - ((right - left + 1) // 2)
        elif c == 'R':
            left = left + ((right - left + 1) // 2)
        if left == right:
            col = right
            break
        index += 1
    seat_id = row * 8 + col
    cabin[(row,col)]  = seat_id
    if seat_id > highest:
        highest = seat_id
        print(highest)
s = sorted(cabin.items())
print(s)
for y in range(128):
    for x in range(8):
        seat_id = cabin.get((y,x), 'missing')
        if seat_id == 'missing':
            seat_id = y * 8 + x
            if seat_id-1 in cabin.values() and seat_id+1 in cabin.values():
                cabin[(y, x)] = y*8+x
                print('Seat ({},{}): {}'.format(y,x,cabin.get((y,x), 'missing')))
                exit()
