import datetime

birth_year = int(input("Enter the year of birth: "))
birth_month = int(input("Enter the month of birth: "))
birth_day = int(input("Enter the day of birth: "))

birth_date = datetime.date(birth_year, birth_month, birth_day)

week_day = birth_date.strftime("%A")


print("The weekday of the birth date is:",week_day)
