import random


my_numbers = [random.randint(1, 1000) for _ in range(100)]

numbers_dict = {'even': 0, 'odd': 0}
for num in my_numbers:
    if num % 2 == 0:
        numbers_dict['even'] += 1
    else:
        numbers_dict['odd'] += 1

print(numbers_dict)
