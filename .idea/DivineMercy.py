Employee_name = input("Enter Employee name :")
hours_of_worked = int(input("Enter numbers of hours worked in a week:"))
Hourly_pay_rate = float(input("Enter pay rate:"))
gross_pay = hours_of_worked * Hourly_pay_rate
federal_withholding_rate = int(input("Enter federal tax: "))
state_withholding_rate = int(input("Enter state tax : "))

print()
print("Employee name is :", Employee_name)
print("Hours worked is  " , hours_of_worked)
print("Hourly pay rate ", Hourly_pay_rate)
print("Gross pay is " ,gross_pay)
print("Deduction")
print("Federal withholding " , federal_withholding_rate*gross_pay/100)
print("State withholding " , state_withholding_rate*gross_pay/100)
print("Total deduction is ",(federal_withholding_rate*gross_pay/100 + state_withholding_rate*gross_pay/100))
print("Net pay is " , gross_pay-(federal_withholding_rate*gross_pay/100 + state_withholding_rate*gross_pay/100 ))


