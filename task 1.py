# 1. Დაწერეთ პროგრამა რომელიც მიიღებს true ან false. Თუ პროგრამამ მიიღო true
# , ეკრანზე დაბეჭდეთ “whoala”.
User_input=input('please enter true or false: ')
if User_input=="true":
    print('whoala')
elif User_input=='false':
    print('input is false')

else:
    print('please reenter')