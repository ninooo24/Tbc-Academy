n = int(input("Please enter the n between 0-10: "))

while n <= 0 or n > 10:
    n = int(input("Please enter the correct number: "))

i = 0
while i <= n:
    print('  ' * (n - i), end='')

    j = i
    while j >= 0:
        print(j, end=' ')
        j = j - 1
    j = 1
    while j <= i:
        print(j, end=' ')
        j = j + 1
    print()
    i = i + 1

