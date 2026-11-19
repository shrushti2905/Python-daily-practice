# Update the price of a product in a dictionary and display all products.

products = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1200
}

products["Mouse"] = 650

for product, price in products.items():
    print(product, ":", price)