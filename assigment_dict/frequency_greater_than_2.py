def frequency_greater_than_two(lists: list):
    counter_lists = []
    convert_to_list = []
    for index in range(len(lists)):
        element = lists[index]
        elements_counter = lists.count(element)

        if elements_counter > 2:
            counter_lists.append(element)
            convert_to_set = set(counter_lists)
            convert_to_list = list(convert_to_set)

    return convert_to_list

