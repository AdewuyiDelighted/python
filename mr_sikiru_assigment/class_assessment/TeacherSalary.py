def teacher_salary():
    salary = 0
    name = input("Enter the teacher name")
    period_taught = int(input("Enter the period spent "))
    rate = 20
    if period_taught > 100:
        extra_period = period_taught - 100
        extra_period_pay = extra_period * 25
        salary = extra_period_pay + rate * 100
    elif period_taught <= 100:
        salary = period_taught * rate

    return print(f'Teacher: {name} \nPeriods:{period_taught} \nGross Salary:{salary}')


print(teacher_salary())
