language = input("Enter your Language : ")
match language:
    case "yoruba":
        print("Welcome to ibadan")
    case "ibo":
        print("Welcome to anambra")
    case "hausa":
        print("Welcome to kano")
    case _:
        print("you are not from here")
