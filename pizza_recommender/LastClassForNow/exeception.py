try:
    with open("demo1.txt", mode='r') as datas:
        for data in datas:
            a, *b = data.split()
            print(a, *b)
except FileNotFoundError:

    print("Make sure you check your file spellings")
print("program execution continues...")

try:
    age = int(input("Enter your age"))
    result = 10 / age
    print(result)
except ZeroDivisionError:
    pass
except ValueError:
    print("ur age cannot be string literal")
finally:
    # the keyword finally helps run whether there is exception or not you can also use it add close to your file
    # after all exception input
    print("finally block runs either there is exception")

# tuple can be used to combine exceptions
# like below:
try:
    age = int(input("Enter your age"))
    result = 10 / age
    print(result)
except (ZeroDivisionError, ValueError, KeyboardInterrupt):
    print("ur age cannot be string literal")
finally:
    # the keyword
    # finally helps run whether there is exception or not you can also use it add close to your file
    # after all exception input
    print("finally block runs either there is exception")


# Raising exception
def age_check(n):
    if n <= 0:
        raise ValueError("age cannot be less than or equal")
    return f'you are {n} years old'
