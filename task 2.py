import datetime

current_year = datetime.datetime.now().year
print(current_year)

Name=input('შეიყვანეთ სახელი: ')
Birth_Year=int(input('შეიყვანეთ დაბადების წელი:'))
print('გამარჯობა,',Name,'თქვენ ხართ',Birth_Year-current_year,'წლის')