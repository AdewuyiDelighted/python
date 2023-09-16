from unittest import TestCase
from mr_sikiru_assigment import logistics


class Test(TestCase):
    def test_rider_wage(self):
        total = logistics.rider_wage(80)
        self.assertEqual(45000, total)

    def test_rider_wage_lesser_50(self):
        amount = logistics.rider_wage(45)
        self.assertEqual(12200, amount)

    def test_rider_wage_lesser_59(self):
        amount = logistics.rider_wage(56)
        self.assertEqual(16200, amount)

    def test_rider_wage_lesser_69(self):
        amount = logistics.rider_wage(68)
        self.assertEqual(22000, amount)
