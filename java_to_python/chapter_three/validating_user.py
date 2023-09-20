passes = 0
failure = 0
for student in range(10):
    score = int(input("Enter student score(1 = pass,2=fail):)"))
    if score == 1:
        passes += 1
    elif score == 2:
        failure += 1
    else:
        score = int(input("(Invalid score)Enter student score(1 = pass,2=fail):)"))
print(passes)
print(failure)
