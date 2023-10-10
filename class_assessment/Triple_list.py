def triple_list(numbers: list):

    total = []
    multiply = 0
    for num in numbers:
        multiply = num * num * num
        total.append(multiply)
    return total
