from datetime import datetime
import json
import os
def main ():
    menu = {
        "pizza": 120,
        "cheese": 40,
        "burger": 70,
        "salad": 25,
        "drink": 10
    }

    users_file="users_file.json"
    history_file="history_file.json"

    if os.path.exists(user_path):
        with open(users_file,"r") as f:
            users=json.load(f)
    else:
        users={}

    if os.path.exists(history_path):
        with open(history_file,"r")as f :
            order_history=json.load(f)
    else:
        order_history={}
    basket={}





    def authenticate():
        print("Welcome to Fast food order manager")
        user_name = input("Enter your name: ").strip()
        password = input("Enter your password: ").strip()

        if user_name in users:
            if users[user_name]==password:
                print("Login successful")
            else:
                print("Wrong password")
                exit()
        else:
            print("New user , registering")
            users[user_name] = password
            with open(users_file,"w") as f:
                json.dump(users, f )
            print("Registered and Loggedin ")
    def show_menu():
        for item in menu.keys():
            print(f"{item}: {menu[item]}")

    def add_basket(username,item):
        if item in menu:
            users[username][item]=users[username].get(item,0)+1
            print(f"{item}: added to your basket")
        else:
            print("your item does not exist")

    def show_basket():

        if not basket:
            print("Your basket is empty ")
            return
        else:
            total = 0
            for item, count in basket.items():
                price = menu.get(item, 0) * count
                print(f"{item} *{count} = {price}")
                total += price
            print(f"total : {total:.2f}")
    def save_basket(username):

        now=datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        basket=users[username]
        total=0
        if not basket:
            print("Your basket is empty ")
            return
        with open("all_users_basket.txt","a") as file:
            file.write(f"Username: {username}\tTime : {now} \n ")
            for item,count in basket.items():
                price = menu[item]*count
                file.write(f"{item} *{count} = {price}\n")
                total += price
            file.write(f"Total : {total:.2f}")
            file.write("-"*40+"\n")
        print("Order saved in all_users_basket.txt")
    def remove_basket(username,item):
        if item in users[username]:
            users[username][item]-=1
            if users[username][item] == 0:
                 users[username].pop(item)
            print(f"{item}: removed from your basket")
        else:
            print("Item not in basket")
    def clear_basket(username):
        users[username].clear()
        print("Basket cleared.")
    while True:
        print("Welcome to Fast food order manager")
        username = input("Enter your username: ")

        if username not in users:
            users[username]={}
        command = input("Choose\n [menu , add , remove , show , save , clear , quit ]: \n").strip().lower()
        if command == "menu":
            show_menu()
        elif command == "add":
            add_item = input("Item you want to add: ").strip().lower()
            add_basket(username,add_item)
        elif command == "remove":
            remove_item = input("Item you want to remove: ").strip().lower()
            remove_basket(username,remove_item)
        elif command == "show":
            show_basket(username)
        elif command == "quit":
            confirm=input("Are you sure you want to quit? [y/n] ").strip().lower()
            if confirm == "y":
                print("Thanks you ! Here is your receipt : ")
                show_basket(username)
                save_basket(username)
            break
        elif command == "clear":
            clear_basket(username)
        elif command == "save":
            save_basket(username)
        else:
            print("invali command")

if __name__ == "__main__":
    main()