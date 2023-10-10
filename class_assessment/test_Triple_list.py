from unittest import TestCase

from class_assessment.Triple_list import triple_list


class Test(TestCase):
    def test_triple_list(self):
        number = [3, 7, 2, 6, 5]
        answer = [27, 343, 8, 216, 125]
        result = triple_list(number)
        self.assertEqual(answer, result)
