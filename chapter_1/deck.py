import collections
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self.cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]

my_card = Card("A", "spades")

test =Card(rank='2', suit='diamonds')
test4 = Card(rank='A', suit='clubs')


my_deck = FrenchDeck()
print(len(my_deck))

print(my_deck[25])

print(choice(my_deck))

print(my_deck[-3:])

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_index = FrenchDeck.ranks.index(card.rank)
    val = rank_index * len(suit_values) + suit_values[card.suit]
    return val

def per_suit(card):
    rank_index = FrenchDeck.ranks.index(card.rank)
    val = rank_index + 13 * suit_values[card.suit]
    return val


for card in sorted(my_deck, key=spades_high):
   print(card)

for card in sorted(my_deck, key=per_suit):
    print(card)
