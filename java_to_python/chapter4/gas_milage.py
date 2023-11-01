class GasMiles:
    def _init_(self, miles, gallons, total, combined_miles):
        self._miles = miles
        self._gallons = 0
        self._total = total
        self._combined_miles = combined_miles

    def set_miles(self, miles):
        self._miles = miles

    def get_miles(self):
        return self._miles

    def set_gallon(self, litres):
        self._gallons = litres

    def get_gallon(self):
        return self._gallons

    def miles_per_gallons(self):
        return self._miles / self._gallons

