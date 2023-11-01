def list_to_dictionary(lists: list):
    empty_dict = {}
    for alpa in lists:
        empty_dict.update({alpa[0]: alpa})
    return (empty_dict)


lists = ["apple", "banana", "coconut"]
print(list_to_dictionary(lists))
