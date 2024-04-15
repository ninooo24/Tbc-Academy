n = int(input("Please enter n 100-1000: "))
if n < 100 or n >= 1000:
    print("incorrect number ")
    exit(1)
else:
    counter = 0
    for i in range(1, n):
        if i % 13 == 0:
            counter = counter + 1
            print(i)
    print("Quantity of i - ", counter)

