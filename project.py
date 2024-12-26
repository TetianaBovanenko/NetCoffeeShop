import json

class CoffeeShop:
    def __init__(self):
        self.menu = {
            "Black Coffee": 2.5,
            "Espresso": 3.0,
            "Latte": 4.0,
            "Cappuccino": 4.5,
        }
        self.orders = []

    def display_menu(self):
        print("\nHere's our menu:")
        print(f"{'Item':<15} {'Price':>6}")
        print("-" * 25)
        for item, price in self.menu.items():
            print(f"{item:<15} ${price:>5.2f}")
        print()

    def validate_menu_choice(self, choice):
        if choice not in self.menu:
            print("Sorry, we don't have that item. Please choose again.")
            return False
        return True

    def get_quantity(self):
        while True:
            quantity = input("How many would you like? ")
            if not quantity.isdigit() or int(quantity) <= 0:
                print("Invalid quantity. Please enter a positive number.")
            else:
                return int(quantity)

    def take_order(self, name):
        order_details = {}
        while True:
            self.display_menu()
            order = input("Please enter your choice from the menu (or type 'done' to finish): ").strip()
            if order.lower() == 'done':
                if not order_details:
                    print("You haven't ordered anything. Please order at least one item.")
                    continue
                break
            if not self.validate_menu_choice(order):
                continue
            quantity = self.get_quantity()
            order_details[order] = order_details.get(order, 0) + quantity
            print(f"Added {quantity} {order}(s) to your order.")
        self.orders.append((name, order_details))
        return order_details

    def calculate_total(self, order_details):
        return sum(self.menu[item] * quantity for item, quantity in order_details.items())

    def generate_receipt(self, name, order_details):
        print(f"\nReceipt for {name}:")
        print(f"{'Item':<15} {'Qty':>5} {'Total':>10}")
        print("-" * 30)
        for item, quantity in order_details.items():
            price = self.menu[item]
            print(f"{item:<15} {quantity:>5} ${price * quantity:>9.2f}")
        total = self.calculate_total(order_details)
        print("-" * 30)
        print(f"{'Total':<15} {'':>5} ${total:>9.2f}\n")

    def log_order(self, name, order_details):
        with open("orders_log.json", "a") as file:
            order_data = {
                "customer": name,
                "order": order_details,
                "total": self.calculate_total(order_details),
            }
            file.write(json.dumps(order_data) + "\n")

    def run(self):
        print("Hello, welcome to NetCoffeeShop!")
        while True:
            name = input("What is your name? ").strip()
            print(f"Hello {name}, thank you for coming in today!")
            order_details = self.take_order(name)
            self.generate_receipt(name, order_details)
            self.log_order(name, order_details)
            another_customer = input("Is there another customer? (yes/no) ").strip().lower()
            if another_customer != 'yes':
                print("Thank you for visiting NetCoffeeShop! Have a great day!")
                break


if __name__ == "__main__":
    shop = CoffeeShop()
    shop.run()
