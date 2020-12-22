

if __name__ == '__main__':
    puzzle_input = open('day_22.in').read().split('\n\n')
    player1 = [int(num) for i, num in enumerate(puzzle_input[0].split('\n')) if i]
    player2 = [int(num) for i, num in enumerate(puzzle_input[1].split('\n')) if i]

    while player1 and player2:
        card1 = player1.pop(0)
        card2 = player2.pop(0)

        if card1 > card2:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)

    winner = player1 if player1 else player2
    winner.reverse()
    total = 0
    for i, card in enumerate(winner):
        total+= (i+1) * card
    print(total)


