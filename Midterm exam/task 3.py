import random


def user_choice():
    user_input = input("Please enter 'R', 'P' or 'S': ")
    print("Users choice is: ", user_input)
    return user_input


def computer_choices():
    choices = ["R", "P", "S"]
    computer_choice = random.choice(choices)
    print("Computer choice is: ", computer_choice)
    return computer_choice


def main():
    if user_choice() == computer_choices():
        print("It is tie")

    elif user_choice() == "R" and computer_choices() == "S":
        print("You are winner")
    elif user_choice() == "S" and computer_choices() == "P":
        print("You are winner")
    elif user_choice() == "P" and computer_choices() == "R":
        print("You are winner")
    elif computer_choices() == "R" and user_choice() == "S":
        print("Computer is winner")
    elif computer_choices() == "S" and user_choice() == "P":
        print("Computer is winner")
    elif computer_choices() == "P" and user_choice() == "R":
        print("Computer is winner")


if __name__ == '__main__':
    main()


