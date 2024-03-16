n = int(input("Please enter n between 0-10000: "))
while n <= 0 or n > 10000:
    n = int(input("Please enter the correct number: "))

reversed_num = 0
sum_of_digits = 0

while n > 0:
    sum_of_digits += n % 10
    reversed_num = reversed_num * 10 + n % 10
    n //= 10

print("reversed number is:", reversed_num)
print("sum of digits:", sum_of_digits)
