from unittest import TestCase

from java_to_python.chapter4.tax_calculator import TaxCalculator


class TestTaxCalculator(TestCase):
    def test_tax_when_earning_is_30000(self):
        taxcalculator = TaxCalculator()
        income = 30000
        result = taxcalculator.calculate_tax_rate(income)
        self.assertEqual(0.15,result)

    def test_tax_when_earning_is_greater_30000(self):
            taxcalculator = TaxCalculator()
            income = 40000
            result = taxcalculator.calculate_tax_rate(income)
            self.assertEqual(0.20, result)