user_input = input("Please enter the text: ")
user_input = user_input.lower()
user_input = user_input.replace(" ","")

if user_input.isalpha():
    if user_input[::] == user_input[::-1]:
        print("Output: Is palindrome")

    else:
        print("Output: Is not palindrome")
else:
    print("Please enter a text containing only alphabetic characters.")

