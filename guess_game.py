import random
number = int(input("Guess a  number between 1 - 10: "))
sum = random.randint(1 , 10)
print(sum)
if sum == number:
    print("You are correct")
else:
    while number !=sum:
        number = int(input("Guess a  between 1 - 10: "))
        sum = random.randint(1, 10)
        print(sum)
        if sum == number:
            print("Your head correct bby")



