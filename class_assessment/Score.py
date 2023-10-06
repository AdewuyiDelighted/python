number = 0
score = []
score[number] = int(input("Enter a number "))
total = score[number]
for num in range(1, 10):
    score[number] = int(input("Enter a number "))
    total += score[number]
print(total)
