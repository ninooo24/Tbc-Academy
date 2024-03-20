user_input = input("Please enter text: ")

i = 0
while i < len(user_input):
    if len(user_input) % 2 == 0:
        if i == 0:
            print(user_input[i] * 5, end=" ")
        elif i == len(user_input) - 1:
            print(user_input[i] * 5, end=" ")
        elif i == len(user_input) // 2 - 1:
            print((user_input[i] + user_input[i + 1]) * 5, end=" ")
    else:
        if i == 0 or i == len(user_input) - 1 or i == len(user_input) // 2:
            print(user_input[i] * 5, end=" ")

    i += 1
