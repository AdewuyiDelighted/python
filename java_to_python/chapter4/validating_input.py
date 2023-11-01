student_counter = 0
passes = 0
failure = 0

while student_counter < 10:
    score = int(input("Enter your grade(1 = pass,2 = fail)"))
    if score == 1:
        passes += 1
    elif score == 2:
        failure += 1
    else:
        score = int(input("Invalid input "+"Enter your grade(1 = pass,2 = fail"))
    student_counter += 1

print("The number of student(s) tat pass: ",passes)
print("The number of student(s) that failed :",failure)


