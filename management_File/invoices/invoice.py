import datetime
class Invoice:
    def __init__(self, invoice_id, costumer_id, Items, date=None):
        self.invoice_id = invoice_id
        self.costumer_id = costumer_id
        self.Items = Items
        self.date = date or datetime.datetime.now().strftime('%Y-%m-%d')
    