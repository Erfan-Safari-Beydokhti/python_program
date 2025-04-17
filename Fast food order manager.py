menu={
    "pizza":120,
    "cheese":40,
    "burger":70,
    "salad":25,
    "drink":10
}
basket={}
def show_menu():
    for item in menu.keys():
        print(f"{item}: {menu[item]}")