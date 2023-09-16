age = int(input("Enter your age: "))


maximum_heart_rate = 220 - age
targeted_heart_rate_one = maximum_heart_rate * 0.5
targeted_heart_rate_two = maximum_heart_rate * 0.85

print(maximum_heart_rate)
print("The range of your heart rate is between",targeted_heart_rate_one,"to",targeted_heart_rate_two)