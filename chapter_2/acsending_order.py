number1 = int(input("Enter a number"))
number2 = int(input("Enter another number"))
number3 = int(input("Enter a number again"))
if number1 > number2 > number3:
    print(number1, number2, number3)
if number2 > number1 > number3:
    print(number2, number1, number3)
if number3 > number1 > number2:
    print(number3, number1, number2)
if number1 > number3 > number2:
    print(number1, number3, number2)
if number2 > number3 > number1:
    print(number2, number3, number1)
if number3 > number2 > number1:
    print(number3, number2, number1)

