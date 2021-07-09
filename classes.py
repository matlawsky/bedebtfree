class Debt:
    def __init__(self, id, title, to_whom, how_much, date, paid=False, paid_off=0) -> None:
        self.id = id
        self.title = title
        self.to_whom = to_whom
        self.how_much = int(how_much)
        self.date = date
        self.paid = paid
        self.paid_off = paid_off

    def to_dict(self) -> dict:
        dictionary = {
            "id": self.id,
            "title": self.title,
            "to_whom": self.to_whom,
            "how_much": self.how_much,
            "date": self.date,
            "paid": self.paid,
            "paid_off": self.paid_off
        }
        return dictionary

class Payment:
    def __init__(self, id, reciever, amount, date) -> None:
        self.id = id
        self.reciever = reciever
        self.amount = int(amount)
        self.date = date
    
    def to_dict(self) -> dict:
        dictionary = {
            "id": self.id,
            "reciever": self.reciever,
            "amount": self.amount,
            "date": self.date
        }
        return dictionary