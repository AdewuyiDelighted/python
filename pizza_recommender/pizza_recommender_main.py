from pizza_recommender_function import *

pizza = Pizza()

pizza_size = int(input("""
***** WELCOME TO RARE PIZZA *****
                This's a Pizza recommending app,helps to let you know the number of pizza boxes you would need
                                
                Enter the Size of pizza you a want
                1.Large size has 10 slices of delicious pizza
                2.Medium size has 6 slices of delicious pizza
                3.Small size has 4 slices of delicious pizza"""))
while pizza_size < 1 or pizza_size > 3:
    print("Invalid input")

    pizza_size = int(input("""
    ***** WELCOME TO RARE PIZZA *****
                    This's a Pizza recommending app,helps to let you know the number of pizza boxes you would need

                    Enter the Size of pizza you a want
                    1.Large size has 10 slices of delicious pizza
                    2.Medium size has 6 slices of delicious pizza
                    3.Small size has 4 slices of delicious pizza"""))
if 1 <= pizza_size <= 3:
    number_super_hungry = int(input("How many Super hungry people would eat pizza"))

    number_hungry = int(input("How many hungry people would eat pizza"))

    number_classic = int(input("How many classic people would eat pizza"))

    slice_for_super_hungry = super_hungry(number_super_hungry)
    slice_for_hungry = hungry_size(number_hungry)
    slices_for_classic = classic_size(number_classic)

    number_of_slices_to_buy = total_number_of_slices(slice_for_super_hungry, slice_for_hungry, slices_for_classic)

    number_of_boxes_needed = number_of_boxes(number_of_slices_to_buy, pizza_size)

    remaining_slices = number_of_slices_remaining(number_of_slices_to_buy, number_of_boxes_needed, pizza_size)

    pizza_prices = prices_of_pizza_boxes(pizza_size)
    total_price_of_pizza = pizza_prices * number_of_boxes_needed

    print("""
    f'The total slices of pizza you would need is {}:
    The total number of boxes you need is {}
    The remaining slices of pizza you would have is {}
    The price of the pizza you would need is {}
    THANKS FOR PATRONAGE'""".format(number_of_slices_to_buy,number_of_boxes_needed,remaining_slices,total_price_of_pizza))