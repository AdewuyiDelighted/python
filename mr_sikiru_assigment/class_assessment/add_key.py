sample = {0: 10, 1: 20}

sample[2] = 30

print(sample)


# funtion

def add_key_value(diction: dict, keys, values):
    diction[keys] = values
    return diction


diction = sample
keys = 5
values = 25
print(add_key_value(diction, keys, values))
