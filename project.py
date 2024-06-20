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
        print("Here's our menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price:.2f}")

    def take_order(self, name):
        order_details = {}
        while True:
            self.display_menu()
            order = input("Please enter your choice from the menu (or type 'done' to finish): ").strip()
            if order.lower() == 'done':
                break
            if order not in self.menu:
                print("Sorry, we don't have that item. Please choose again.")
                continue
            quantity = input(f"How many {order}(s) would you like? ")
            if not quantity.isdigit():
                print("Invalid quantity. Please enter a number.")
                continue
            quantity = int(quantity)
            if order in order_details:
                order_details[order] += quantity
            else:
                order_details[order] = quantity
        self.orders.append((name, order_details))

    def calculate_total(self, order_details):
        total = 0
        for item, quantity in order_details.items():
            total += self.menu[item] * quantity
        return total

    def generate_receipt(self, name, order_details):
        print(f"\nReceipt for {name}:")
        for item, quantity in order_details.items():
            price = self.menu[item]
            print(f"{item} (x{quantity}): ${price * quantity:.2f}")
        total = self.calculate_total(order_details)
        print(f"Total: ${total:.2f}\n")

    def log_order(self, name, order_details):
        with open("orders_log.txt", "a") as file:
            file.write(f"Order for {name}:\n")
            for item, quantity in order_details.items():
                file.write(f"{item} (x{quantity}): ${self.menu[item] * quantity:.2f}\n")
            total = self.calculate_total(order_details)
            file.write(f"Total: ${total:.2f}\n\n")

    def run(self):
        print("Hello, welcome to NetCoffeeShop!")
        while True:
            name = input("What is your name? ").strip()
            print(f"Hello {name}, thank you for coming in today!")
            self.take_order(name)
            for name, order_details in self.orders:
                self.generate_receipt(name, order_details)
                self.log_order(name, order_details)
            another_customer = input("Is there another customer? (yes/no) ").strip().lower()
            if another_customer != 'yes':
                print("Thank you for visiting NetCoffeeShop! Have a great day!")
                break

if __name__ == "__main__":
    shop = CoffeeShop()
    shop.run()
