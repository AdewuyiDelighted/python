from list_function.assignment import Card_validator

card_number = input("Kindly Enter your Card Details to verify:")
length = Card_validator.account_number_length(card_number)
while length < 13 or length > 16:
    card_number = input("Incorrect number(Kindly Enter your Card Detail to verify:")
    length = Card_validator.account_number_length(card_number)
if 13 <= length <= 16:
    print("*********************************")
    print("*Credit Card Type :", end=" ")
    Card_validator.return_message(card_number)
    print("*Credit Card Number: " + card_number)
    print("*Credit Card Digit Length: ", length)
    print("*Credit Card Validity Status: " ,end=" ")
    Card_validator.check_card_validity(card_number)
    print("************************************")
