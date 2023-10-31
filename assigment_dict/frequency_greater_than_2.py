def frequency_greater_than_two(lists: list):
    counter_lists = []
    for index in range(len(lists)):
        element = lists[index]
        elements_counter = lists.count(element)

        if elements_counter > 2:
            counter_lists.append(element)
            convert_to_set = set(counter_lists)
            convert_to_list = list(convert_to_set)

    print(convert_to_list)


lists = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]
print(frequency_greater_than_two(lists))
