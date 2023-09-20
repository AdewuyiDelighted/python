principal = int(input("Enter your principal:$"))
rate = 0.1
year = 30

#for year in range(1, 31, 1):
    #roi = rate * principal
    #total = principal * (1 + 0.1)
    #principal = total
    #print(f"your ROI is  ${roi:.2f} ,your investment is ${total:.2f} , in year{year}")

    #another method
for year in range (1,31):
    roi = principal * rate
    new_amount = principal + roi
    principal = new_amount
    print(f"your ROI is  ${roi:.2f} ,your investment is ${new_amount:.2f} , in year{year}")

