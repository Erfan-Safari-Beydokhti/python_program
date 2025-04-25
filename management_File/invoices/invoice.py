import datetime
class Invoice:


    def __init__(self, invoice_id, customer_id, Items, date=None):
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.Items = Items
        self.date = date or datetime.datetime.now().strftime('%Y-%m-%d')


    def total_price(self):
        return sum(item["price"] * item["quantity"] for item in self.Items)


    def to_dict(self):
        return {
            "invoice_id": self.invoice_id,
            "customer_id": self.customer_id,
            "Items": self.items,
            "date": self.date,
            "total_price": self.total_price()
        }


    def from_dict(data):
        return Invoice(
            data["invoice_id"],
            data["customer_id"],
            data["items"],
            data.get("date")
        )