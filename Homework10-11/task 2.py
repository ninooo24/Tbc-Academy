import random
import math
n = int(input("Enter n(n>1): "))
while n <= 0:
    n = int(input("Please enter the correct number: "))

counter = 0
for i in range(0, n):
    a = random.random()
    b = random.random()
    if math.sqrt(a ** 2 + b ** 2) <= 1:
        counter += 1

output = 4 * counter / n
print("output is ", output)

#n-ის ზრდასთან ერთად მიისწრაფის pi-სკენ
