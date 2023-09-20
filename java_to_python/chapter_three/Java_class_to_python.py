class Native:
    def __init__(self, name, scv_id, balance):
        self._name = name
        self._Scv_id = scv_id
        self._balance = balance

    def set_name(self, name):
        self._name = name

    def __get_name(self):
        return self._name

    def __get_balance(self):
        return self._balance

    def __set_deposit(self, amount):
        self._balance += amount

    def __get_deposit(self):
        return self.check_balance
