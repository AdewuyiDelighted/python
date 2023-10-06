import unittest

from list_function.function import largest
from list_function.function import reverse
from list_function.function import check_element
from list_function.function import oddlyplaced
from list_function.function import evenly_placed
from list_function.function import running_total
from list_function.function import palindrome
from list_function.function import sum_for_loop
from list_function.function import concatenates
from list_function.function import combine_elements


class MyTestCase(unittest.TestCase):
    def test_something(self):
        number = [1, 10, 100]
        answer = 100
        result = largest(number)
        self.assertEqual(answer, result)

    def test_for_number_greater(self):
        numbers = [2000, 5000, 100000]
        result = largest(numbers)
        self.assertEqual(result, 100000)

    def test_for_reversed(self):
        number = [1, 2, 3, 4]
        answer = [4, 3, 2, 1]
        result = reverse(number)
        self.assertEquals(answer, result)

    def test_that_function_check_element(self):
        number = [1, 2, 3, 4, 5, 6]
        element = 5
        answer = True
        result = check_element(number, element)
        self.assertTrue(answer, result)

    def test_number_are_oddly_placed(self):
        number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        answer = [2, 4, 6, 8]
        result = oddlyplaced(number)
        self.assertEqual(answer, result)

    def test_number_are_evenly_placed(self):
        number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        answer = [1, 3, 5, 7, 9]
        result = evenly_placed(number)
        self.assertEqual(answer, result)

    def test_running_sum(self):
        number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        answer = 55
        result = running_total(number)
        self.assertEqual(answer, result)

    def test_if_a_number_is_a_palindrome(self):
        name = 'Tosin'
        answer = palindrome(name)
        self.assertFalse(answer)

    def test_sum_using_for_loop(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        answer = 55
        result = sum_for_loop(numbers)
        self.assertEqual(answer, result)

    def test_concatenation(self):
        numberb = ['1', '2', '3', '4', '5']
        letter = ['a', 'b', 'c', 'd', 'e']
        answer = ['1', '2', '3', '4', '5', 'a', 'b', 'c', 'd', 'e']
        result = concatenates(numberb, letter)
        self.assertEqual(answer, result)

    def test_function_of_combined_element(self):
        numberb = ['a', 'b', 'c', 'd', 'e']
        letter = ['1', '2', '3', '4', '5']
        answer = ['a', '1', 'b', '2', 'c', '3', 'd', '4', 'e', '5']
        result = combine_elements(numberb, letter)
        self.assertEqual(answer, result)

# if __name__ == '__main__':
#   unittest.main()
