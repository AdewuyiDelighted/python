count_mile = 0
count_gallon = 0
miles = 1
# miles = int(input("Enter the mile driven(Enter -1 to stop):"))
# gallon = int(input("Enter the gallon of fuel used:"))
while miles > 0:
    miles = float(input("Enter the mile driven(Enter -1 to stop):"))
    count_mile += miles
    gallon = float(input("Enter the gallon of fuel used):"))
    count_gallon += gallon
    mile_per_gallon = gallon / miles
    print(f'{mile_per_gallon}')
combined_miles_per_gallon = count_gallon / count_mile
print(combined_miles_per_gallon)
