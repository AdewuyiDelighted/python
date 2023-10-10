from unittest import TestCase

from list_function.assignment import Card_validator


class Test(TestCase):
    def test_account_number_length(self):
        number = "4388576018410707"
        answer = 16
        result = Card_validator.account_number_length(number)
        self.assertEqual(answer, result)

    def test_confirm_account_number_function(self):
        numbers = "4388576018402626"
        answer = 37
        result = Card_validator.confirm_account_number(numbers)
        self.assertEqual(answer, result)

    def test_the_oddly_placed_numbers_in_card_numbers(self):
        numbers = "4388576018402626"
        answer = 38
        result = Card_validator.oddly_placed_number(numbers)
        self.assertEqual(answer,result)

    def test_the_combine_function(self):
        numbers = "4388576018402626"
        answer = 75
        result = Card_validator.combine(numbers)
        self.assertEqual(answer, result)







