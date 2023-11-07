from unittest import TestCase

from pizza_recommender import pizza_recommender_function


class Test(TestCase):
    def test_the_initial_number_of_slices_for_super_hungry(self):
        answer = pizza_recommender_function.super_hungry(1)
        self.assertEqual(4, answer)

    def test_the_initial_number_of_slices_for_hungry(self):
        answer = pizza_recommender_function.hungry_size(1)
        self.assertEqual(2, answer)

    def test_the_initial_number_of_slices_for_classic(self):
        answer = pizza_recommender_function.classic_size(1)
        self.assertEqual(1, answer)

    def test_the_number_of_slices_if_there_is_more_than_one_super_hungry_eater(self):
        number_of_eater = 4
        answer = pizza_recommender_function.super_hungry(number_of_eater)
        result = 16
        self.assertEqual(result, answer)

    def test_the_number_of_slices_if_there_is_more_than_one_hungry_eater(self):
        number_of_eater = 6
        answer = pizza_recommender_function.hungry_size(number_of_eater)
        result = 12
        self.assertEqual(result, answer)

    def test_the_number_of_slices_if_there_is_more_than_one_classic_hungry_eater(self):
        number_of_eater = 5
        answer = pizza_recommender_function.classic_size(number_of_eater)
        result = 5
        self.assertEqual(result, answer)

    def test_the_number_of_boxes_needed_if_large_size_was_order(self):
        answer = pizza_recommender_function.number_of_boxes(28, 1)
        self.assertEqual(3, answer)

    def test_the_number_of_boxes_needed_if_medium_size_was_order(self):
        answer = pizza_recommender_function.number_of_boxes(35, 2)
        self.assertEqual(6, answer)

    def test_the_number_of_boxes_needed_if_small_size_was_order(self):
        answer = pizza_recommender_function.number_of_boxes(19, 3)
        self.assertEqual(5, answer)

    def test_that_function_return_the_remaining_if_there_is_excess_in_large_size(self):
        answer = pizza_recommender_function.number_of_slices_remaining(25, 3, 1)
        self.assertEqual(5, answer)

    def test_that_function_return_the_remaining_if_there_is_excess_in_medium_size(self):
        answer = pizza_recommender_function.number_of_slices_remaining(47, 8, 2)
        self.assertEqual(1, answer)

    def test_that_function_return_the_remaining_if_there_is_excess_in_small_size(self):
        answer = pizza_recommender_function.number_of_slices_remaining(46, 12, 3)
        self.assertEqual(2, answer)

    def test_price_of_large_size(self):
        answer = pizza_recommender_function.prices_of_pizza_boxes(1)
        self.assertEqual(6000, answer)

    def test_price_of_medium_size(self):
        answer = pizza_recommender_function.prices_of_pizza_boxes(2)
        self.assertEqual(3000, answer)

    def test_price_of_small_size(self):
        answer = pizza_recommender_function.prices_of_pizza_boxes(3)
        self.assertEqual(1200, answer)
