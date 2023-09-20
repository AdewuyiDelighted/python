number = int(input("Enter a number:"))
total = number
sum = 0
divide = 1
convert = 0
if 10000 <= number < 99999:
    while number != 0:
        divide = number % 10
        convert = convert * 10 + divide
        number /= 10

if total == convert:
    print(number, "is a palindrome")
