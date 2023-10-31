from unittest import TestCase

from ChaperFour.arbitrary_argument import calculate_product


class Test(TestCase):
    def test_calculate_product(self):
        result = calculate_product(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.assertEqual(3628800, result)
