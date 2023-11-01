target = int(input("Enter your number"))
count = 0
while target != 0:
    user_input = int(input("Enter another number"))
    count += user_input
    if count >= target:
        print(True)
        break
