from unittest import TestCase

from list_function.assignment.mulitply_list import multiply


class Test(TestCase):
    def test_multiply(self):
        number = [2, 3, 4, 5, 6, ]
        self.assertEqual(720, multiply(number))
