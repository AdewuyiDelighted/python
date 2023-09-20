class Account:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def set_deposit(self,amount):
        self._balance += amount

    def get_deposit(self):
        return self._balance
