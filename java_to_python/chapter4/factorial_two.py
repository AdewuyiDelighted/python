number = int(input("Enter a number"))
product = 1
divide = 0
add = 1
for num in range(number+1):
    if num == 0:
        continue
    product *= num
    divide = 1/product
    add += divide
print(add)



