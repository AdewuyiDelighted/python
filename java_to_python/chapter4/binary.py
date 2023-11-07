str_numbers = input("Enter a number")
total = 1
base = 2

for num in range(len(str_numbers) + 1):
    total *= 10

int_number = int(str_numbers)

digit_one = int_number / total
divide = total / 10

sums = digit_one * base

int_divide = int(divide)

for num in range(int_divide,0,10):
    total_two = int_number / num % 10
    sums += total_two
    sums *= base
over_all = sums / 2

print(over_all)
