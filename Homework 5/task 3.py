size = int(input("Enter tree size between 1-50: "))
if size <= 0 or size > 50:
    print("Please enter the valid number between 1 and 50.")
else:
    left_side = '/'
    right_side = '\\'
    top = '*'
    middle = '|'

    for i in range(size):
        spaces = (size - i - 1) * ' '
        if i == 0:
            print(spaces + top)
        else:
            branches = i * left_side + middle + i * right_side
            print(spaces + branches)

    print(" " * (size - 1) + "|")

