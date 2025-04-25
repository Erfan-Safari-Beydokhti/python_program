import json
import os
from customers.customer import Customer

Data_path="data\customers.json"
def load_customers():
    if not os.path.exists(Data_path):
        return []
    with open(Data_path, "r") as f:
        try:
            data=json.load(f)
            return [Customer.from_dict(c) for c in data]
        except json.JSONDecodeError:
            return[]
def save_customers(customers):

    with open(Data_path, "w") as file:
        json.dump([c.to_dict() for c in customers], file,indent=4)
def add_customer():
    customers = load_customers()
    print("\n افزدون مشتری جدید ")
    id=len(customers)+1
    name=input("نام مشتری:").strip()
    phone=input("شماره تلفن مشتری:").strip()
    email=input("ایمیل مشتری:").strip()
    new_customer=Customer(id,name,phone,email)
    customers.append(new_customer)

    save_customers(customers)
    print("مشتری با موفقیت اضافه شد ")

def list_customers():
    customers = load_customers()
    if not customers:
        print("لیستی از مشتری ها وجود ندارد")
        return
    print("لیست مشتری ها ")
    for c in customers:
        print(f"id:{c.id} , name:{c.name} , phone:{c.phone} , email:{c.email}")
    print()
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