
from java_to_python.chapter4.tax_calculator import TaxCalculator

taxcalculator = TaxCalculator()
for num in range(3):
    name = input("Enter name of citizen")
    income = int(input("Enter the citizen income"))

    print(taxcalculator.calculate_tax_rate(income))

