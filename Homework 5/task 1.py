n = int(input("Enter the number between 0-50: "))

if n <= 0 or n > 50:
    print('please enter the correct number')
else:
    for i in range(1, n):
        print(i, "-", end="")
        count = 0
        for j in range(1, i):
            if i % j == 0:
                count = count + 1
                if count <= 3:
                    print(j, end=" ")
        print()



