
def rider_wage(collection_rate):
    if collection_rate < 50:
        return collection_rate * 160 + 5000
    elif collection_rate < 59:
        return collection_rate * 200 + 5000
    elif collection_rate < 69:
        return collection_rate * 250 + 5000
    else:
        return collection_rate * 500 + 5000






#wages = int(input("Enter the riders collection rates"))
#total = rider_wage(wages)
#print(total)
