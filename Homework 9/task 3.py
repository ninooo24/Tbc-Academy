input_date = input("Input: ")

date_time, timezone = input_date.split('+')
date, time = date_time.split('T')
year, month, day = date.split('-')
hour, minute, second = time.split(':')
timezone = timezone[:-3] + ' ' + timezone[-2:]

print(f"Output: {day}-{month}-{year} {hour}:{minute}:{second} {timezone}")
