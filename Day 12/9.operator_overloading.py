class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance
    
wlt1 = Wallet(10)
wlt2 = Wallet(30)

print(wlt1 + wlt2)
