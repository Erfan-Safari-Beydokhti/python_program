import json
import os
from customers.customer import Customer

def main():
    while True:
        print("\n سیستم مدیریت مشتری و فاکتور :")
        print("1. افزودن مشتری جدید")
        print("2. مشاهده لیست مشتری ها")
        print("3. افزودن فاکتور جدید ")
        print("4. مشاهده فاکتور ها")
        print("5. خروج")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            pass
        elif choice=="2":
            pass
        elif choice=="3":
            pass
        elif choice=="4":
            pass
        elif choice =="5":
            print("Exiting ...")
            break
        else:
            print("Invalid option")
if __name__ == "__main__":
    main()