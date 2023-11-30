# w used for writing
# a used for append
# r used to read from file
# you can creat file by used w and a too
# w+ used to perform both read and write


# file = open("demo.txt", mode='w')
# file.write("Ope is a short girl\n")
# file.write("uye is a man beater\n")
# file.write("Tobi is sweet husband to ope\n")
# file.close()
#
with open("demo.txt", mode='a') as file:
    file.write("Welcome to c18")


with open("demo.txt", mode='r') as file:
    for record in file:
        first, second, *third = record.split()
        print(f'{first:<10}{second:<10}{third}')
