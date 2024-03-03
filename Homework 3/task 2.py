import datetime

birth_year = int(input("Enter the year of birth: "))
birth_month = int(input("Enter the month of birth(1-12): "))
birth_day = int(input("Enter the day of birth(1-31): "))


if birth_year<0 or birth_year>2024:
    print('pleas enter the valid year')
elif birth_month>12 or birth_month<0:
    print('please enter the valid month ')
elif birth_day>31 or birth_day<0:
    print('please enter the valid day')
else:
    birth_date = datetime.date(birth_year, birth_month, birth_day)
    week_day = birth_date.strftime("%A")
    print("The weekday of the birth date is:", week_day)






