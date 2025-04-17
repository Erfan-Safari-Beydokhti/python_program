def main ():
    menu = {
        "pizza": 120,
        "cheese": 40,
        "burger": 70,
        "salad": 25,
        "drink": 10
    }
    basket = {}

    def show_menu():
        for item in menu.keys():
            print(f"{item}: {menu[item]}")

    def add_basket(item):
        if item in menu:
            basket[item] = basket.get(item, 0) + 1
            print(f"{item}: added to your basket")
        else:
            print("your item does not exist")

    def show_basket():
        if not basket:
            print("Your basket is empty ")
        else:
            total = 0
            for item, count in basket.items():
                price = menu.get(item, 0) * count
                print(f"{item} *{count} = {price}")
                total += price
            print(f"total : {total}")

    def remove_basket(item):
        if item in basket:
            basket[item] -= 1
        if basket[item] == 0:
            basket.pop(item)

    while True:
        command = input("Choose\n [menu , add , remove , show , quit]: \n").strip().lower()
        if command == "menu":
            show_menu()
        elif command == "add":
            add_item = input("Item you want to add: ").strip().lower()
            add_basket(add_item)
        elif command == "remove":
            remove_item = input("Item you want to remove: ")
            remove_basket(remove_item)
        elif command == "show":
            show_basket()
        elif command == "quit":
            print("Thanks you ! Here is your receipt : ")
            show_basket()
            break
        else:
            print("invali command")

if __name__ == "__main__":
    main()