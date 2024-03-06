n = int(input('please enter n between 0-20: '))
if n < 0 or n > 20:
    print('please enter n between 0-20')

a = 0
b = 1
for i in range(n):
    a, b = b, a+b

print(a)
