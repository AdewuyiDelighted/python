total = 0
counter = 0
score = int(input("Enter your score or -1 to quit"))
while score != -1:
    total += score
    counter += 1
    score = int(input("Enter your score or -1 to quit"))
average = total/counter
print(f"The average of the grade is {average}")
