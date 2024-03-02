car_speed=int(input('enter the car speed: '))
if 30<car_speed<60:
    print('Moderate')
elif 60<car_speed<120:
    print('fast')
elif car_speed>120:
    print('very fast')
else:
    print('slow')