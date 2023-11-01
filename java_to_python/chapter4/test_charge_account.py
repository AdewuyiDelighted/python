from unittest import TestCase

from java_to_python.chapter4.charge_account import ChargeAccount


class TestChargeAccount(TestCase):
    def test_that_customer_have_account(self):
        charge_account = ChargeAccount()
        charge_account.set_account_number(2126903496)
        self.assertEqual(2126903496,charge_account.get_account_number())

    def test_that_customer_have_balance(self):
        charge_account = ChargeAccount()
        charge_account.set_balance(0)
        self.assertEqual(0,charge_account.get_balance())

    def test_the_total_amount_of_the_item(self):
        charge_account = ChargeAccount()
        charge_account.set_purchase(6000)
        self.assertEqual(6000,charge_account.get_purchase())

    def test_total_amount_of_credit_paid(self):
        charge_account = ChargeAccount()
        charge_account.set_credit(2000)
        self.assertEqual(2000,charge_account.get_credit())

    def test_account_credit_limit(self):
        charge_account = ChargeAccount()
        charge_account.get_credit_limit()
        self.assertEqual(5000,charge_account.get_credit_limit())

    def test_Account_can_calculate_new_balance(self):
        charge_account = ChargeAccount()
        charge_account.set_purchase(6000)
        charge_account.set_credit(2500)
        charge_account.get_new_balance()
        self.assertEqual(3500,charge_account.get_new_balance())


