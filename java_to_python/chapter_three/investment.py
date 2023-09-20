principal = 1000
rate = 0.07
year = 30

for year in range(1, 31):
    total = principal * (1 + rate) ** year

    print(f"year{year} \t return\t{total}")
    