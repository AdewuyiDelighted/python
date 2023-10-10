from unittest import TestCase

from list_function.assignment.sum_list import sums


class Test(TestCase):
    def test_sums(self):
        num = [15, 20, 25, 20, 10, 5]
        self.assertEquals = (95, sums(num))
