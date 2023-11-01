def remove_element(lists: list):
    object = ""
    filled_list = []
    for string in lists:
        if string != object:
            filled_list.append(string)
        else:
            continue
    return (filled_list)


lists = ["", "A,B,C", "x,y,z", "a,b,c","","XYZ"]
print(remove_element(lists))
