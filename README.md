🧾 Customer & Invoice Management System
A simple command-line Python project to manage customers and invoices. It allows users to add customers, create invoices, and view saved records. Data is stored in JSON format with a clean and modular code structure.

📦 Features
Add new customers (ID, Name, Email, Phone)

Create invoices with multiple items (name, price, quantity)

Save each invoice to a separate JSON file

View all invoices and customers

Error handling for file operations

Modular and maintainable project structure

🗂️ Project Structure

<pre> ```
invoice_manager/ 
├── customers/ 
│ └── customer.py # Logic for customer data (class/functions) 
│ 
├── invoices/ 
│ └── invoice.py # Logic for invoice creation and data handling 
│ 
├── data/ 
│ ├── customers.json # All customer records stored here 
│ └── invoices/ # Each invoice saved as a separate JSON file 
│ 
├── main.py # Entry point to run the app 
└── README.md # Project description and documentation ``` </pre>
