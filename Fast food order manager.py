from datetime import datetime
import json
import os

def main():
    menu = {
        "pizza": 120,
        "cheese": 40,
        "burger": 70,
        "salad": 25,
        "drink": 10
    }

    users_file = "users_file.json"
    history_file = "history_file.json"

    if os.path.exists(users_file):
        with open(users_file, "r") as f:
            users = json.load(f)
    else:
        users = {}

    if os.path.exists(history_file):
        with open(history_file, "r") as f:
            order_history = json.load(f)
    else:
        order_history = {}

    basket = {}

    def authenticate():
        print("Welcome to Fast food order manager")
        user_name = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        if user_name in users:
            if users[user_name] == password:
                print("Login successful")
            else:
                print("Wrong password")
                exit()
        else:
            print("New user, registering")
            users[user_name] = password
            with open(users_file, "w") as f:
                json.dump(users, f)
            print("Registered and Logged in")
        return user_name

    def show_menu():
        print("\nMenu:")
        for item, price in menu.items():
            print(f"{item}: {price}")
        print()

    def add_basket(item):
        if item in menu:
            basket[item] = basket.get(item, 0) + 1
            print(f"{item} added to your basket")
        else:
            print("This item does not exist in menu")

    def show_basket():
        if not basket:
            print("Your basket is empty")
        else:
            total = 0
            print("Your Basket:")
            for item, count in basket.items():
                price = menu[item] * count
                print(f"{item} x{count} = {price}")
                total += price
            print(f"Total: {total}\n")

    def save_basket(username):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        order = {
            "date": now,
            "items": basket.copy(),
            "Total": sum(menu[item] * count for item, count in basket.items())
        }
        order_history.setdefault(username, []).append(order)
        with open(history_file, "w") as f:
            json.dump(order_history, f, indent=4)
        print("Order saved!")

    def show_order_history(username):
        if username not in order_history or not order_history[username]:
            print("Your order history is empty\n")
            return
        for order in order_history[username]:
            print(f"Date: {order['date']}")
            for item, count in order["items"].items():
                print(f"  {item} x{count}")
            print(f"  Total: {order['Total']}")
            print("-" * 30)

    def remove_basket(item):
        if item in basket:
            basket[item] -= 1
            if basket[item] == 0:
                del basket[item]
            print(f"{item} removed from your basket")
        else:
            print("Item not in basket")

    def clear_basket():
        basket.clear()
        print("Basket cleared.")

    username = authenticate()

    while True:
        command = input("Choose [menu, add, remove, show, save, clear, history, quit]: ").strip().lower()
        if command == "menu":
            show_menu()
        elif command == "add":
            add_item = input("Item to add: ").strip().lower()
            add_basket(add_item)
        elif command == "remove":
            remove_item = input("Item to remove: ").strip().lower()
            remove_basket(remove_item)
        elif command == "show":
            show_basket()
        elif command == "save":
            save_basket(username)
        elif command == "clear":
            clear_basket()
        elif command == "history":
            show_order_history(username)
        elif command == "quit":
            confirm = input("Are you sure you want to quit? (y/n): ").strip().lower()
            if confirm == "y":
                print("Thank you! Here is your receipt:")
                show_basket()
                break
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
