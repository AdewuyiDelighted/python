number = 1
count_odd = 0
count_even = 0
while number <= 9:
    if number % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
    number += 1
numb = "[1,2,3,4,5,6,7,8,9]"
print(f"Sample numbers:numbers = {numb}", "\n" "Expected Output:", "\n", f"Number of even number:{count_even}", "\n",
      f"Number of odd number: {count_odd}")
