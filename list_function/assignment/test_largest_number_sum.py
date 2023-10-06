from unittest import TestCase

from list_function.assignment.largest_number_sum import largest


class Test(TestCase):
    def test_largest(self):
        number = [2, 5, 10, 17, 3, 30, 3]
        self.assertEqual(30, largest(number))
