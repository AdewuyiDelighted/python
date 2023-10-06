from unittest import TestCase

from list_function.assignment.sum_list import sums


class Test(TestCase):
    def test_sums(self):
        num = [2, 3, 4, 5, 6, 7, 8, 10]
        self.assertEquals = (45, sums(num))
