password = 'TBC_Academy'
MAX_TRIES = 3

for i in range(MAX_TRIES):
    input_password = input('Please enter password: ')
    if input_password == password:
        print('Welcome to TBC')
        break
    else:
        if i == 2:
            print("You are blocked")
            break
        else:
            print("Password is incorrect, please try again")

print()

