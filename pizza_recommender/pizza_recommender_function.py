import math


class Pizza:
    LARGE_SIZE_SLICES = 10
    MEDIUM_SIZE_SLICES = 6
    SMALL_SIZE_SLICES = 4


def super_hungry(numberOfThem: int):
    return numberOfThem * 4


def hungry_size(numberOfThem: int):
    return numberOfThem * 2


def classic_size(numberOfThem: int):
    return numberOfThem * 1


def total_number_of_slices(super_hungry: int, hungry_size: int, classic_size: int):
    return super_hungry + hungry_size + classic_size


def number_of_boxes(total_number_of_slices: int, size):
    total_number_of_boxes = 0.0

    if size == 1:
        total_number_of_boxes = total_number_of_slices / Pizza.LARGE_SIZE_SLICES
    elif size == 2:
        total_number_of_boxes = total_number_of_slices / Pizza.MEDIUM_SIZE_SLICES
    elif size == 3:
        total_number_of_boxes = total_number_of_slices / Pizza.SMALL_SIZE_SLICES
    elif size != 1 or size != 2 or size != 3:
        total_number_of_boxes = 0
    return math.ceil(total_number_of_boxes)


def number_of_slices_remaining(total_slices, number_of_boxes, size):
    number_of_remainder = 0
    if size == 1:
        number_of_remainder = Pizza.LARGE_SIZE_SLICES * number_of_boxes - total_slices
    elif size == 2:
        number_of_remainder = Pizza.MEDIUM_SIZE_SLICES * number_of_boxes - total_slices
    elif size == 3:
        number_of_remainder = Pizza.SMALL_SIZE_SLICES * number_of_boxes - total_slices
    elif size != 1 or size != 2 or size != 3:
        number_of_remainder = 0
    return number_of_remainder


def prices_of_pizza_boxes(size):
    prices_per_box = 0
    if size == 1:
        prices_per_box = 6000
    elif size == 2:
        prices_per_box = 3000
    elif size == 3:
        prices_per_box = 1200
    else:
        return prices_per_box
    return prices_per_box
