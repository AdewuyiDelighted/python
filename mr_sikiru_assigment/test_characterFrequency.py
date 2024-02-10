from unittest import TestCase

from mr_sikiru_assigment import characterFrequency


class Test(TestCase):
    def test_count_element(self):
        input = "semicolon.africa"
        expected = {'s': 1, 'e': 1, 'm': 1, 'i': 2, 'c': 2, 'o': 2, 'l': 1, 'n': 1, '.': 1, 'a': 2, 'f': 1, 'r': 1}
        self.assertEqual(expected,characterFrequency.countElement(input))

    def test_count_shorter_element(self):
        input = "delighted"
        expected = {'d': 2, 'e': 2, 'l': 1, 'i': 1, 'g': 1, 'h': 1, 't': 1}
        self.assertEqual(expected, characterFrequency.countElement(input))



