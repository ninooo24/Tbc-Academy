import random

_symbols = ["Clubs", "Diamonds", "Hearts", "Spades"]
_values = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

random_symbols = random.choice(_symbols)
random_values = random.choice(_values)

print("Random card is:", random_values, random_symbols)

