number = 10
count = 1
product = 1
divide = 0
sum = 1

while count <= number:
    product *= count
    divide = float(1 / product)
    sum += divide
    count += 1

print(sum)
