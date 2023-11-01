from unittest import TestCase

from assigment_dict import difference_highest_lowest


class Test(TestCase):
    def test_differences(self):
        lists = [10,75,20,30,15,5,40,25,40,35]
        answer = 70
        result = difference_highest_lowest.differences(lists)
        self.assertEqual(answer,result)

    def test_the_differences_btween_list_largest_smallest(self):
        lists = [100,2,5,26,234,125,307]
        answer = 305
        result = difference_highest_lowest.differences(lists)
        self.assertEqual(answer, result)
