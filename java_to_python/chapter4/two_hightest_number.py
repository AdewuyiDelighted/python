number = 0
highest = number
highest_two = number
for n in range(10):
    number = int(input("Enter a number"))
    if number > highest_two and number < highest:
        highest_two = number

    if number > highest:
        highest_two = highest
        highest = number

print("The two highest number is ", highest, "and", highest_two)
