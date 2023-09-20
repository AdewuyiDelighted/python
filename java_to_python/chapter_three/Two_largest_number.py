count = 1
counter = 0
highest_one = 0
highest_two = 0

for count in range(9):
    number = int(input("Enter a number : "))
    if number > highest_two and number < highest_one:
        highest_two = number

    if number > highest_one:
        highest_two = highest_two
        highest_one = number
print("The two highest is ", highest_one, highest_two)
