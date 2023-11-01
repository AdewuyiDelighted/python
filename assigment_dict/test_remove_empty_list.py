from unittest import TestCase

from assigment_dict import remove_empty_list


class Test(TestCase):
    def test_remove_element(self):
        lists = ["", "A,B,C", "x,y,z", "a,b,c","","XYZ"]
        expected = ["A,B,C","x,y,z","a,b,c","XYZ"]
        result = remove_empty_list.remove_element(lists)
        self.assertEqual(expected,result)
