import random


def guess_game():
    stopper = 1
    while stopper != -1:
        user_input = int(input("Guess a number"))
        answer = random.randrange(1, 5)
        if user_input > answer:
            print("Too high.Try again")
        elif user_input < answer:
            print("Too small.Try again")
        elif user_input == answer:
            print("Congratulation.you guessed the number")
            stopper = int(input("Enter - 1 to stop or 0 to continue"))


print(guess_game())
