def remove_duplicate(numbers: list):
    list_set = set(numbers)
    sort_list = sorted(list_set)
    print(sort_list)


num = [1, 2, 1, 4, 2, 4, 6, 8, ]
remove_duplicate(num)
