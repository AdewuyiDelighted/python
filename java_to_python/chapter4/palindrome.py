numbers = int(input("Enter a five digits numbers"))
divide = 10000
convert = ""
while 1000 > numbers > 99999:
    numbers = int(input("Enter a five digits numbers"))

if numbers > 9999:
    while numbers != 0:
        digit_one = numbers / divide % 10
        divide /= 10
        str_digit_one = str(digit_one)
        convert += str_digit_one + ""

print(convert)
