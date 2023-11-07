def list_to_dictionary(lists: list):
    empty_dict = {}
    for alpa in lists:
        letter = alpa[0]
        if letter in empty_dict:
            letter = alpa[0].upper()
        empty_dict.update({letter: alpa})
    return empty_dict


lists = ["apple", "banana", "coconut","corn"]
print(list_to_dictionary(lists))
