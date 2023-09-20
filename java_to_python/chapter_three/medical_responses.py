doctor_question_one = bool(input("What your problem(if yes enter 1 or if  enter 0):"))
if doctor_question_one:
    doctor_question_two = bool(input("Have your had this problem before (enter 1 for yes or ignore if no)?"))
    if doctor_question_two:
        print("Well,you have it again")
    else:
        print("Well,you have it now")

