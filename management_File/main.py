import json
import os
from customers.customer import Customer
import uuid
from invoices.invoice import Invoice


Data_path="data/customers.json"


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


def create_invoice():
    print("صدور فاکتور جدید")
    customer_id=input("شماره کاربری مشتری:").strip()
    customers=load_customers()
    if not any(c.id == int(customer_id)for c in customers):
        print("مشتری با این شماره کاربری پیدا نشد")
        return
    items=[]
    while True:
        name=input("نام محصول : ( پایان )برای خروج").strip()
        if name =="پایان":
            print("پایان صدور فاکتور")
            break
        try:
            price=float(input("قیمت محصول را وارد کنید:"))
            quantity=int(input("تعداد محصول:"))
            items.append({"name":name,"price":price,"quantity":quantity})
            print(f" با موفقیت اضافه شد{name}")
        except ValueError:
            print("ورودی نامعتبر")
    invoice_id=str(uuid.uuid4())[:8]
    invoice=Invoice(invoice_id,customer_id,items)
    invoice_path=f"data/invoices/invoice_{customer_id}.json"
    with open(invoice_path, "w") as file:
        json.dump(invoice.to_dict(),file,indent=4)
    print(f"ثبت شد{invoice_id}فاکتور با شناسه ")


def list_invoices():
    print("لیست فاکتور ها")
    invoice_folder="data/invoices"
    files=os.listdir(invoice_folder)
    if not files:
        print("هیچ فاکتوری وجود ندارد")
        return
    for file in files:
        file_path=os.path.join(invoice_folder,file)
        with open(file_path, "r") as file:
            data=json.load(file)
            invoice=Invoice.from_dict(data)
            print(f" فاکتور {invoice.invoice_id} | مشتری {invoice.customer_id} | تاریخ {invoice.date} | مبلغ کل: {invoice.total_price():,.0f} تومان ")
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
            add_customer()
        elif choice=="2":
            list_customers()
        elif choice=="3":
            create_invoice()
        elif choice=="4":
            list_invoices()
        elif choice =="5":
            print("Exiting ...")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()