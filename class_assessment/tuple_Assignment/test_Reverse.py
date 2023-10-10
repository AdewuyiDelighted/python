from unittest import TestCase
from class_assessment.tuple_Assignment import Tuple


class Test(TestCase):
    def test_reverse_tuple(self):
        num = (10, 20, 30, 40, 50)
        result = (50, 40, 30, 20, 10)
        answer = Tuple.reverse_tuple(num)
        self.assertEqual(result, answer)

    def test_unpacked_elements(self):
        num = 15, 25, 60, 50, 30, 40, 45, 50
        result = (50, 15)
        answer = Tuple.unpack(num)
        self.assertEqual(result, answer)
