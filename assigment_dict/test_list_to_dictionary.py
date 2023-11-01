from unittest import TestCase

from assigment_dict.list_to_dictionary import list_to_dictionary


class Test(TestCase):
    def test_list_to_dictionary(self):
        lists = ['apples','banana','coconut']
        expected = {'a': 'apples','b':'banana','c':'coconut'}
        result = list_to_dictionary(lists)
        self.assertEqual(expected,result)
