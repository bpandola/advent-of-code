
class Hand:

    types = {
        'FIVE': 7,
        'FOUR': 6,
        'FULL': 5,
        'THREE': 4,
        'TWO': 3,
        'ONE': 2,
        'HIGH': 1,
    }

    card_to_value = {
        'T': 10,
        'J': 0, # 11, for part 1
        'Q': 12,
        'K': 13,
        'A': 14,
    }
    def __init__(self, parsed):
        hand, bet = parsed
        self.bet = bet
        self.hand = [int(self.card_to_value.get(card, card)) for card in hand]
        self.determine_type(self.hand)


    def determine_type(self, hand):
        dups = {}
        for card in hand:
            if card not in dups:
                dups[card] = 1
            else:
                dups[card] = dups[card]+1
        values = list(dups.values())
        if 5 in values:
            self.type_ = 'FIVE'
        elif 4 in values:
            self.type_ = 'FOUR'
        elif 3 in values and 2 in values:
            self.type_ = 'FULL'
        elif 3 in values:
            self.type_ = 'THREE'
        elif values.count(2) == 2:
            self.type_ = 'TWO'
        elif 2 in values:
            self.type_ = 'ONE'
        else:
            self.type_ = 'HIGH'
        # Part 2
        if self.card_to_value["J"] in dups:
            num_jacks = dups[self.card_to_value["J"]]
            if self.type_ == 'FOUR':
                self.type_ = 'FIVE' # fuck it was rihht here! if num_jacks == 1 else 'FOUR'
            elif self.type_ == 'FULL':
                self.type_ = 'FIVE' # if num_jacks in (2,3) else 'FULL'
            elif self.type_ == 'THREE':
                self.type_ = 'FOUR' if num_jacks in (1,3) else 'FIVE' if num_jacks == 2 else 'THREE'
            elif self.type_ == 'ONE':
                self.type_ = 'THREE' if num_jacks == 2 else 'THREE' if num_jacks == 1 else 'ONE'
            elif self.type_ == 'HIGH':
                self.type_ = 'ONE'
            elif self.type_ == 'TWO':
                self.type_ = 'FOUR' if num_jacks == 2 else 'FULL' if num_jacks == 1 else 'TWO'
            else:
                self.type_ = self.type_
        print(self.type_)

    def __repr__(self):
        return f"{self.type_}"

    def __str__(self):
        return f"{self.type_}"


lines = open('day_07.in').read().split('\n')
hands = [Hand(tuple(line.split())) for line in lines]

def compare(item1, item2):
    if item1.type_ != item2.type_:
        return Hand.types.get(item1.type_) - Hand.types.get(item2.type_)
    index = 0
    while True:
        value1, value2 = item1.hand[index], item2.hand[index]
        if value1 == value2:
            index +=1
            continue
        return value1 - value2
from functools import cmp_to_key
hands_sorted = sorted(hands, key=cmp_to_key(compare))
score = 0
for i,hand in enumerate(hands_sorted):
    print(f"{hand.type_} {hand.hand} {hand.bet} {i+1}")
    score += int(hand.bet) * (i+1)
print(score)
assert score == 250577259, score

