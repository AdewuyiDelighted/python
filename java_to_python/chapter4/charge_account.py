class ChargeAccount:
    def _init_(self):
        self._account_number = 0
        self._purchase = 0
        self._credit = 0
        self._total_balance = 0

    def set_account_number(self, account_number):
        self._account_number = account_number

    def get_account_number(self):
        return self._account_number

    def set_balance(self,amount):
        self._total_balance = amount

    def get_balance(self):
        return self._total_balance

    def set_purchase(self,amount):
        self._purchase = amount

    def get_purchase(self):
        return self._purchase

    def set_credit(self,amount):
        self._credit = amount

    def get_credit(self):
        return self._credit

    def get_credit_limit(self):
        return 5000

    def get_new_balance(self):
        return  self._purchase - self._credit
