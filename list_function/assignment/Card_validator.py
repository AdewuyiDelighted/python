def account_number_length(card_number: str):
    length = len(card_number)
    return length


def confirm_account_number(card_number: str):
    count = " "
    counts = 0
    product = 0
    sums = 0
    length = account_number_length(card_number)
    for index in range(length - 2, 0 - 1, -2):
        count = card_number[index]
        counts = int(count)
        product = 2 * counts
        if product > 9:
            numberone = product // 10
            numbertwo = product % 10
            product = numberone + numbertwo
        sums += product
    return sums


def oddly_placed_number(card_number: str):
    count = " "
    counts = 0
    sums = 0
    length = account_number_length(card_number)
    for index in range(length - 1, 0, -2):
        count = card_number[index]
        counts = int(count)
        sums += counts
    return sums


def combine(card_numbers: str):
    total = confirm_account_number(card_numbers)
    totaltwo = oddly_placed_number(card_numbers)
    sums = total + totaltwo
    return sums


def check_card_validity(card_numbers: str):
    result = combine(card_numbers)
    if result & 10 == 0:
        print("Card number is valid")
    else:
        print("Card Number is Invalid")


def return_message(card_numbers: str):
    if card_numbers[0] == "4":
        print("Visa Card")
    elif card_numbers[0] == "5":
        print("Master Card")
    elif card_numbers[0] == "3" and card_numbers[1] == "7":
        print("American Express Card")
    elif card_numbers[0] == "6":
        print("Discover Card")
    else:
        print("Invalid Card")



