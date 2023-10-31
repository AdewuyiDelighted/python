def return_dictionary(listOne: list, listTwo: list):
    contain_dict = {}
    count = 0
    for n in listTwo:
        contain_dict.update({listOne[count]: n})
        count += 1
    print(contain_dict)


input1 = ['a', 'b', 'c', 'd', 'e']
input2 = [1, 2, 3, 4, 5]
print(return_dictionary(input1, input2))
