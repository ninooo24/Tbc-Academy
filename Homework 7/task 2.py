n = int(input("Please enter n between 0-1000: "))
while n <= 0 or n > 1000:
    n = int(input("Please enter the correct number: "))

print(n, end="")

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print("->", n, end="")

