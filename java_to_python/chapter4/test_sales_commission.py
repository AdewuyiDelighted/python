from unittest import TestCase

from java_to_python.chapter4.sales_commission import SalesCommission


class TestSalesCalculator(TestCase):
    def test_that_sales_people_wages(self):
        sales_commission = SalesCommission()
        sales_commission.set_wage()
        self.assertEqual(200,sales_commission.get_wage())

    def test_the_total_sales_of_sales_person(self):
        sales_commission = SalesCommission()
        sales_commission.set_sales(7500)
        self.assertEqual(7500,sales_commission.get_sales())

    def test_the_total_commission_0f_sales_persons(self):
        sales_commission = SalesCommission()
        sales_commission.set_sales(7500)
        sales_commission.get_total_commission()
        self.assertEqual(875.0,sales_commission.get_total_commission())


