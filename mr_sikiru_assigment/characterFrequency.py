def countElement(input: str):
    element_dict = {}
    for element in input:
        counts = input.count(element)
        element_dict[element] = counts

    return element_dict


print(countElement("semicolon.africa"))
