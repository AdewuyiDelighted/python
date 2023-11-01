class SalesCommission:
    def _init_(self):
        self._sales = 0
        self._wage = 200

    def set_wage(self):
        self._wage = 200

    def get_wage(self):
        return self._wage

    def set_sales(self, sale):
        self._sales = sale

    def get_sales(self):
        return self._sales

    def get_total_commission(self):
        return 200 + (9 * self._sales / 100)
