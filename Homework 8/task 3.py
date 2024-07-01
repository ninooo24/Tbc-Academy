input_str = str(input("enter a string: "))
len_is_even = False
if len(input_str) % 2 == 0:
    mid_index = len(input_str) // 2 - 1
    len_is_even = True
else:
    mid_index = len(input_str) // 2
i = 0
while i < 5:
    if len_is_even:
        print(input_str[0], input_str[mid_index] + input_str[mid_index + 1], input_str[-1])
    else:
        print(input_str[0], input_str[mid_index], input_str[-1])
    i += 1

