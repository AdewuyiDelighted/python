number = 1
add = 0
count = 0

for number in range(0, 51, 2):
    print(number,end=" ")
    count += 1
    add += number

print("The average of is ", add, "is", add / count)
