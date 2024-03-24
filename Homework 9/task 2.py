text_1 = input("Please enter the text: ")
text_2 = input("Please enter the text: ")
for c in text_1:
    if len(text_1) != len(text_2) or text_1.count(c) != text_2.count(c):
        print("Output: No")
        exit()
    else:
        print("Output: Yes")
        exit()
