n = int(input("Enter n(n>1): "))
while n <= 0:
    n = int(input("Please enter the correct number: "))

x = 0
sign = 1
for i in range(1, n+1):
    x += sign * 1 / (2 * i - 1)
    sign *= -1
x *= 4
print(f"x = {x}")

#n-ის ზრდასთან ერთად x მიისწრაფის pi-სკენ
