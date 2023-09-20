#age = input("Enter your age:")
#if age <= "18":
 #   print("You are not eligible to be in this club")
#elif age > "18":
 #   print("You are eligible to be in this club")
#else:
 #   print("Go home joorr")


age = int(input("Enter your age:"))
result = "not eligible" if age <=18 else "Eligible"
print ("You are " + result)