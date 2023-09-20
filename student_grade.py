total = 0
counter = 0
score = 1
while score != 0:
    score = int(input("Enter your score or -1 to quit"))
    total += score
    counter += 1
average = total/counter
print(average)
