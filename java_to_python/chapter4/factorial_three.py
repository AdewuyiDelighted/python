numbers = int(input("Enter a number"))
product = 1
power = 0
divide = 0
add = 0
for num in range(numbers + 1):
    if num == 0:
        continue
    product *= num
    power = numbers ** num

    divide = power / product
    add += divide

print("The constant of e is ", add)
