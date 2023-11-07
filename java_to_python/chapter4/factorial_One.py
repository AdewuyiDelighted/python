number = int(input("Enter a non negative number"))
count = 1
if number < 0:
    print("invalid number")
else:
    for num in range(number +1):
        if num == 0:
            continue
        count *= num
    print(count)
