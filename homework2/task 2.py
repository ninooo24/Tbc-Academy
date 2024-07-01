import datetime

a = int(input('please enter the first natural number: '))
b = int(input('please enter the second natural number: '))
if a <= 0 or b <= 0:
    print("please enter the natural numbers")
else:
    if a % b == 0:
        print(b, 'is multiple for', a)
    else:
        print(b, 'is not multiple for', a)


current_year = datetime.datetime.now().year
print(current_year)

name = input('შეიყვანეთ სახელი: ')
birth_year = int(input('შეიყვანეთ დაბადების წელი:'))
print('გამარჯობა,', name, 'თქვენ ხართ', birth_year - current_year, 'წლის')
