def differences(lists: list):
    maximum = max(lists)
    minimum = min(lists)
    return maximum - minimum


lists = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
print(differences(lists))
