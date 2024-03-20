row1 = "qwertyuiop"
row2 = "asdfghjkl"
row3 = "zxcvbnm"

action = input("Enter action (e/d): ")
if action.lower() not in ['e', 'd']:
    print("Enter correct action")
    exit(1)

user_input = input("Enter text: ").lower()

for char in user_input:
    if char in row1:
        row = row1
    elif char in row2:
        row = row2
    elif char in row3:
        row = row3
    else:
        print(char, end="")
        continue

    index = row.index(char)
    if action.lower() == 'e':
        index = (index + 1) % len(row)
    else:
        index = (index - 1) % len(row)

    print(row[index], end="")

print()

