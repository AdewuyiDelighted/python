from unittest import TestCase

from mr_sikiru_assigment.class_assessment.AddFirstTwoString import swapFirstTwoCharacter


class Test(TestCase):
    def test_swap_first_two_character(self):
        first_input = "abc"
        second_input = "xyz"
        expected = swapFirstTwoCharacter(first_input,second_input)
        self.assertEqual("xyz abz", expected)
