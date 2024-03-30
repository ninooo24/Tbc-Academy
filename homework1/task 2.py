import datetime

current_year = datetime.datetime.now().year
print(current_year)

name = input('შეიყვანეთ სახელი: ')
birth_year = int(input('შეიყვანეთ დაბადების წელი:'))
print('გამარჯობა,', name, 'თქვენ ხართ', birth_year - current_year, 'წლის')
