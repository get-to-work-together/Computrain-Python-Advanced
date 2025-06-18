import random

ranks = '2 3 4 5 6 7 8 9 10 B V H A'.split()
suits = list('♣♦♥♠')

deck = [r + s for s in suits for r in ranks ]

random.shuffle(deck)

hand = sorted([deck.pop() for _ in range(5)], key = lambda card: '♣♦♥♠'.find(card[-1]))

print(hand)