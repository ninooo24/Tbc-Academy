user_input = input("Please enter text: ")

for i in range(len(user_input)):
    if user_input[i] not in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
        print(user_input[i], end="")
print()
