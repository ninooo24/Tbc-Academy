import random

number = int(input("Enter n between 0-30: "))
if number <= 0 or number > 30:
    print('please enter n between 0-30')
else:
    random_numbers = [random.randint(0, 1000) for i in range(number)]
    max_number = max(random_numbers)

    print(random_numbers)
    print(max_number)

