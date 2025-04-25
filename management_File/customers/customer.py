class Customer:
    def __init__(self,id, name, phone, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email
        }


    def from_dict(data):
        return Customer(
            data["id"],
            data["name"],
            data["phone"],
            data["email"]
        )