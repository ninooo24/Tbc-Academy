import json

with open('recipes.json', 'r') as recipes_file:
    recipes = json.load(recipes_file)


with open('available_products_shops.json', 'r') as products_file:
    available_products_shops = json.load(products_file)

desired_recipe = input("Enter the name of the recipe you want to cook: ")

if desired_recipe in recipes:
    required_ingredients = recipes[desired_recipe]

    available_stores = []
    for store, products in available_products_shops.items():
        if all(ingredient in products for ingredient in required_ingredients):
            available_stores.append(store)

    if available_stores:
        print(f"The following stores have all ingredients for {desired_recipe}:")
        for store in available_stores:
            print(store)
    else:
        print(f"Sorry, none of the stores have all ingredients for {desired_recipe}.")
else:
    print("Recipe not found.")
