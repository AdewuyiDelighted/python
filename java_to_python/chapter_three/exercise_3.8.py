number = int(input("Enter a number :"))
sum = 0
count = 0
average = 0
product = 1
largest = 0
smallest = number

for number in range(3):
    number = int(input("Enter a number :"))
    count += 1
    sum += number
    average = sum / count
    product *= number
    if number > largest:
        largest = number
        if number < smallest:
            smallest = number
print(average)
print(sum)
print(product)
print(largest)
print(smallest)
