import datetime
class Invoice:
    def __init__(self, invoice_id, costumer_id, Items, date=None):
        self.invoice_id = invoice_id
        self.costumer_id = costumer_id
        self.Items = Items
        self.date = date or datetime.datetime.now().strftime('%Y-%m-%d')
    def total_price(self):
        return sum(item["price"] * item["count"] for item in self.Items)
    def to_dict(self):
        return {
            "invoice_id": self.invoice_id,
            "costumer_id": self.costumer_id,
            "items": self.Items,
            "date": self.date
            "total_price": self.total_price()
        }