def average(add):
    return sum(add) / len(add)


exam_score = []
for num in range(10):
    add = int(input("Enter a number "))
    exam_score.append(add)
print(average(exam_score))

# abtionary  argument
def average(*add):
    return sum(add) / len(add)


print(average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
