from unittest import TestCase

from assigment_dict import slit_to_half


class Test(TestCase):
    def test_slit_to_two(self):
        lists = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
        expected = [10,75,20,30,15],[5,40,25,40,35]
        result = slit_to_half.slit_to_two(lists)
        self.assertEqual(expected,result)
