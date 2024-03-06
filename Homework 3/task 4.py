import datetime
from forex_python.bitcoin import BtcConverter

_year = int(input('Please enter the year when you bought the bitcoin: '))
_month = int(input('Please enter the month when you bought the bitcoin: '))
_day = int(input('Please enter the day when you bought the bitcoin: '))
_price = float(input('Please enter the price you paid for bitcoin in USD: '))



bought_day = datetime.date(_year, _month, _day)
current_date = datetime.datetime.now()

if _price < 0:
    print("Please enter a valid price (greater than or equal to 0)")

b = BtcConverter()
bought_price = b.get_previous_price('USD', bought_day)
current_price = b.get_latest_price('USD')

if bought_price is None:
    print("Bitcoin price data not available for the specified date.")
else:
    _amount = _price / bought_price
    profit = current_price * _amount - bought_price * _amount

    if profit > 0:
        print("Your profit is", profit)
    else:
        print('Your loss is', profit)