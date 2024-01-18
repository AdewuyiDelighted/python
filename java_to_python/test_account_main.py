from unittest import TestCase

from java_to_python.account_main import Account


class TestAccount(TestCase):
    def testAccountBalance(self):
        my_account = Account(0)
        my_account.get_balance()
        self.assertEqual(0,my_account.get_balance())
