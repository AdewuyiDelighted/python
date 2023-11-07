def add_ing(input):
    add_ring = "ing"
    add_ly = "ly"
    length = len(input)

    if length >= 3:
        if add_ring not in input[-3::]:
            result = input + add_ring
        elif add_ring in input[-3::]:
            result = input + add_ly

    else:
        return input
    return result


print(add_ing("string"))
