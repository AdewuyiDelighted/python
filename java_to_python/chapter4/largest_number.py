counter = 0
largest = 0
for num in range(10):
    number = int(input("Enter number "))
    counter += 1
    if number > largest:
        largest = number

print(largest)


