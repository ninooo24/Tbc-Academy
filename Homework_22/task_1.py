small_data = []
high_data = []

with open('data.txt', 'r') as file:
    for line in file:
        user_name, product_name, amount, price = line.strip().split(',')
        total_price = float(amount) * float(price)
        if total_price < 10:
            small_data.append(line)
        else:
            high_data.append(line)

with open('small.txt', 'w') as small_file:
    small_file.writelines(small_data)

with open('high.txt', 'w') as high_file:
    high_file.writelines(high_data)
