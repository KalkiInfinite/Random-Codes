class Store:
    def __init__(self):
        self.products = {
            'p1': {'name': 'Product 1', 'price': 10},
            'p2': {'name': 'Product 2', 'price': 20},
            'p3': {'name': 'Product 3', 'price': 30},
            'p4': {'name': 'Product 4', 'price': 40},
            'p5': {'name': 'Product 5', 'price': 50},
        }

    def display_menu(self):
        print("Products available:")
        for code, product in self.products.items():
            print(f"{code}: {product['name']} - ${product['price']}")

    def generate_bill(self, quantities):
        total_amount = 0
        print("Bill:")
        for code, product in self.products.items():
            quantity = quantities.get(code, 0)
            if quantity > 0:
                amount = quantity * product['price']
                print(f"{product['name']} - {quantity} x ${product['price']} = ${amount}")
                total_amount += amount
        print(f"Total amount: ${total_amount}")

store = Store()
store.display_menu()

quantities = {}
for code in store.products.keys():
    quantity = int(input(f"Enter quantity required for {code}: "))
    quantities[code] = quantity

store.generate_bill(quantities)
