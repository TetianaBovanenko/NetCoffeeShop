print("Hello, welcome to NetCoffeeShop!")
name = input("What is your name?\n")
print("Hello " + name + ", thank you for coming in today!\n")
menu = {
    "Black Coffee": 2.5,
    "Espresso": 3.0,
    "Latte": 4.0,
    "Cappuccino": 4.5,
}
print(name + ", what would you like from our menu? Here's what we have:")
for item, item_price in menu.items():
    print(f"{item}: ${item_price:.2f}")
order = input("Please enter your choice from the menu: ")
quantity = int(input("How many coffees would you like?\n"))
if order in menu:
    price = menu[order]
    total = price * quantity
    print(f"Thanks, {name}. Your total for {quantity} {order}(s) is ${total:.2f}")
    print("We'll have it ready for you in a moment.")