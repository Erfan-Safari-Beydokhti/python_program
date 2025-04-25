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
    print("\n Add new customer : ")
    id=len(customers)+1
    name=input("Customer's name : ").strip()
    phone=input("Customer's phone number :").strip()
    email=input("Customer's email address : ").strip()
    new_customer=Customer(id,name,phone,email)
    customers.append(new_customer)

    save_customers(customers)
    print("Customer added successfully.")


def list_customers():
    customers = load_customers()
    if not customers:
        print("There is no list of customers.")
        return
    print("Customers list")
    for c in customers:
        print(f"id:{c.id} , name:{c.name} , phone:{c.phone} , email:{c.email}")
    print()


def create_invoice():
    print("Issuance of a new invoice")
    customer_id=input("Customer ID: ").strip()
    customers=load_customers()
    if not any(c.id == int(customer_id)for c in customers):
        print("Customer with this ID was not found.")
        return
    items=[]
    while True:
        name=input("Product Name: (End) for Exit : ").strip()
        if name.lower() =="end":
            print("End of invoice issuance")
            break
        try:
            price=float(input("Enter the product price : "))
            quantity=int(input("Number of products : "))
            items.append({"name":name,"price":price,"quantity":quantity})
            print(f" {name} Added successfully. ")
        except ValueError:
            print("Invalid input")
    invoice_id=str(uuid.uuid4())[:8]
    invoice=Invoice(invoice_id,customer_id,items)
    invoice_path=f"data/invoices/invoice_{customer_id}.json"
    with open(invoice_path, "w") as file:
        json.dump(invoice.to_dict(),file,indent=4)
    print(f"Invoice with ID {invoice_id} registered. ")


def list_invoices():
    print("List of invoices")
    invoice_folder="data/invoices"
    files=os.listdir(invoice_folder)
    if not files:
        print("There is no invoice.")
        return
    for file in files:
        file_path=os.path.join(invoice_folder,file)
        with open(file_path, "r") as file:
            data=json.load(file)
            invoice=Invoice.from_dict(data)
            print(f" Invoice {invoice.invoice_id} | Customer {invoice.customer_id} | Date {invoice.date} | Total amount: {invoice.total_price():,.0f} Toman ")
        print()


def main():
    while True:
        print("\n Customer and Invoice Management System:")
        print("1. Add new customer")
        print("2. View customer list")
        print("3. Add new invoice ")
        print("4. View invoices")
        print("5. Exit")

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