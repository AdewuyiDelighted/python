from unittest import TestCase

from mr_sikiru_assigment.class_assessment import completion_of_string
from mr_sikiru_assigment.class_assessment.completion_of_string import add_ing


class Test(TestCase):
    def test_that_function_add_ing_to_string_without_ing(self):
        inputs = "abc"
        result = add_ing(inputs)
        self.assertEqual("abcing", result)

    def test_that_function_add_ly_to_string_with_ing(self):
            inputs = "string"
            result = add_ing(inputs)
            self.assertEqual("stringly", result)

    def test_that_word_lesser_than_three(self):
        inputs = "ab"
        result = add_ing(inputs)
        self.assertEqual("ab", result)


