def student_names(name):
    student_age = {"dike": 33, "ope": 25, "melody": 20, "precious": 27}
    if name in student_age:
        print(f'Hi {name},you are {student_age.get(name)}')

    else:
        print("Your name is not in the dictionary of the student age")
        enter_age = int(input("Enter your age"))

        student_age.update({name: enter_age})
        print(f'Hi {name},you are {student_age.get(name)}')
        return student_age


print(student_names("john"))
