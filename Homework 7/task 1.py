n = int(input("Please enter n between 0-20: "))
while n <= 0 or n > 20:
    n = int(input("Please enter the correct number: "))

num_1 = 0
num_2 = 1
i = 0

while i < n:
    i += 1
    print(num_1, end=" ")
    summ = num_1 + num_2
    num_1 = num_2
    num_2 = summ
