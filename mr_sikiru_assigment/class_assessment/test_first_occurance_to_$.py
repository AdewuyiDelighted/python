from unittest import TestCase

from mr_sikiru_assigment.class_assessment import first_occurrence


class Test(TestCase):
    def test_convert_first_occurrence_to_a_character(self):
        inputs = "restart"
        answer = first_occurrence.convert_first_occurrence_to_a_character(inputs)
        self.assertEqual("resta$t",answer)

    def test_convert_first_occurrence_to_a_character_two(self):
        inputs = "delighted"
        answer = first_occurrence.convert_first_occurrence_to_a_character(inputs)
        self.assertEqual("delighte$",answer)

    def test_convert_first_occurrence_to_a_character_three(self):
        inputs = "life"
        answer = first_occurrence.convert_first_occurrence_to_a_character(inputs)
        self.assertEqual("life",answer)


