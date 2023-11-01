from unittest import TestCase

from assigment_dict import frequency_greater_than_2


class Test(TestCase):
    def test_frequency_greater_than_two(self):
        lists = [1,1,1,1,2,2,2,2,3,3,5,5,5,6,7]
        expected = [1,2,5]
        result = frequency_greater_than_2.frequency_greater_than_two(lists)
        self.assertEqual(expected,result)

    def test_frequency_greater_that_two_two(self):
        lists = [23,34,46,20,23,23,19,46,7,46,]
        expected = [46,23]
        result = frequency_greater_than_2.frequency_greater_than_two(lists)
        self.assertEqual(expected, result)


