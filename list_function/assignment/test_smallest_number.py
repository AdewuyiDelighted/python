from unittest import TestCase

from list_function.assignment.smallest_number import smallest


class Test(TestCase):
    def test_smallest(self):
        number = [3, 5, 6, 2, 9, 10, 34, ]
        self.assertEqual(2, smallest(number))
