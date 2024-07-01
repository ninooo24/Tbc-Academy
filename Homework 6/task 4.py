n = int(input("Please enter the n between 0-10: "))
while n <= 0 or n > 10:
    n = int(input("Please enter the correct number "))

i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end="")
        j = j + 1
    print()
    i = i + 1

i = n - 1
while i > 0:
    j = 1
    while j <= i:
        print(j, end="")
        j = j + 1
    print()
    i = i - 1
