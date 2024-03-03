import datetime
from forex_python.bitcoin import BtcConverter
_year = int(input('please enter the year when you bought the bitcoin: '))
_month = int(input('please enter the month when you bought the bitcoin: '))
_day = int(input('please enter the day when you bought the bitcoin: '))
_price = float(input('please enter the price you paid for bitcoin in USD: '))

if _year < 0 or _year > 2024:
    print('please enter the valid year')
elif _month > 12 or _month < 0:
    print('please enter the valid month ')
elif _day > 31 or _day < 0:
    print('please enter the valid day')
elif _price < 0:
    print('please enter the valid price')

else:
    bought_day = datetime.date(_year, _month, _day)
    current_date = datetime.datetime.now()

    b = BtcConverter()
    bought_price = b.get_previous_price('USD', bought_day)
    current_price = b.get_latest_price('USD')
    _amount = _price/bought_price
    profit = current_price*_amount-bought_price*_amount
    if profit > 0:
        print("your profit is ",profit)
    else:
        print('your loss is ',profit)
