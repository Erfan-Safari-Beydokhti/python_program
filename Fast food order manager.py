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

def add_basket(item):
    if item in menu:
        basket[item]=basket.get(item,0)+1
        print(f"{item}: added to your basket")
    else:
        print("your item does not exist")

def show_basket():
    if not basket:
      print("Your basket is empty ")
    else:
        total=0
        for item,count in basket.items():
            price=menu.get(item,0)*count
            print(f"{item} *{count} = {price}")
            total+=price
        print(f"total : {total}")