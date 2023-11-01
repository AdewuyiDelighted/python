def slit_to_two(lists: list):
    list_one = []
    list_two = []
    length = len(lists) // 2

    for index in range(length):
        num = lists[index]
        list_one.append(num)

    for indx in range(length, len(lists)):
        num = lists[indx]
        list_two.append(num)

    return list_one, list_two


lists = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
print(slit_to_two(lists))
