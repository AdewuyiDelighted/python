number = 10
row = 1
column = 1
column_one = 1
for row in range(1, 10):
    for column in range(1, row):
        print("*", end=" ")
    print()
    for column in range(1, row):
        print("*", end=" ")
print()
