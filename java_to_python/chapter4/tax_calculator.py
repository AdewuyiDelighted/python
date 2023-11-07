class TaxCalculator:
    def _init_(self):
        self._tax = 0

    def calculate_tax_rate(self,amount):
        if amount == 30000:
            self._tax = 0.15
        elif amount > 30000:
            self._tax = 0.20

        return self._tax
