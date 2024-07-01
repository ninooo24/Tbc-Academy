import json

sales_by_product = {}
total_sales_by_user = {}
total_sales = 0

with open('data.txt', 'r') as file:
    for line in file:
        user_name, product_name, amount, price = line.strip().split(',')
        amount = int(amount)
        price = float(price)

        sales_by_product[product_name] = sales_by_product.get(product_name, 0) + amount
        total_sales_by_user[user_name] = total_sales_by_user.get(user_name, 0) + amount * price
        total_sales += amount * price

max_sales_user = max(total_sales_by_user, key=total_sales_by_user.get)
max_sales_product = max(sales_by_product, key=sales_by_product.get)

average_sales = total_sales / len(sales_by_product)
average_amount = sum(sales_by_product.values()) / len(sales_by_product)

stats = {
    "max_sales_by_product": max_sales_product,
    "max_total_sales_by_user": max_sales_user,
    "average_sales": average_sales,
    "average_amount": average_amount,
    "top_selling_product": max_sales_product
}

with open('stats.json', 'w') as json_file:
    json.dump(stats, json_file, indent=4)
