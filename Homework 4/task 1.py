import random

players = int(input("Enter players number: "))
if players <= 0:
    print('please enter the positive number ')

for i in range(players):
    print(random.randint(1, 6), random.randint(1, 6))


