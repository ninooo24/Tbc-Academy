import random
computer_number = random.randint(0,100)
max_tries = 10
tries = 0

while tries < max_tries:
    user_number = int(input('Please enter the number between 0-100: '))

    if user_number == computer_number:
        print('You are winner')
        break

    elif user_number > computer_number:
        print('Your number is high')

    elif user_number < computer_number:
        print("Your number is low")
    tries = tries + 1

if tries == max_tries:
    print("Computer's number is", computer_number, "Computer is winner")

print('thank you!')



