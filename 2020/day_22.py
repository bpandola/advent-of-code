
def parse_input(filename):
    hands = open(filename).read().split('\n\n')
    hand1 = [int(num) for i, num in enumerate(hands[0].split('\n')) if i]
    hand2 = [int(num) for i, num in enumerate(hands[1].split('\n')) if i]
    return [hand1, hand2]


def play_combat(hands):
    player1, player2 = list(hands[0]), list(hands[1])
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
    winner_score = 0
    for i, card in enumerate(winner):
        winner_score += (i + 1) * card
    return winner_score


def play_recursive_combat(hands):

    def play_game(player_hands):
        p1, p2 = list(player_hands[0]), list(player_hands[1])
        hashed_hands = []
        while p1 and p2:
            hashed_hand = hash(tuple(p1+['terminal']+p2))
            if hashed_hand in hashed_hands:
                # Player 1 automatically wins.
                return p1, []
            else:
                hashed_hands.append(hashed_hand)

            card1 = p1.pop(0)
            card2 = p2.pop(0)

            if card1 <= len(p1) and card2 <= len(p2):
                result, _ = play_game([p1[:card1], p2[:card2]])
            else:
                result = card1 > card2

            if result:
                p1.append(card1)
                p1.append(card2)
            else:
                p2.append(card2)
                p2.append(card1)
        return p1, p2

    player1, player2 = play_game(hands)
    winner = player1 if player1 else player2
    winner.reverse()
    winner_score = 0
    for i, card in enumerate(winner):
        winner_score += (i + 1) * card
    return winner_score


if __name__ == '__main__':
    puzzle_input = parse_input('day_22.in')
    sample_input = parse_input('day_22.in.sample')

    # Part 1
    assert play_combat(sample_input) == 306
    print(play_combat(puzzle_input))

    # Part 2
    assert play_recursive_combat(sample_input) == 291
    print(play_recursive_combat(puzzle_input))
