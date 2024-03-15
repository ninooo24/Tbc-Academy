a = 1
while a < 10:
    b = 1
    while b < a + 1:
        print(f"{b} x {a} = {b*a}", end="\t")
        b = b + 1
    a = a + 1
    print()
