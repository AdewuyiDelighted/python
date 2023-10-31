def count_string(inputs):
    empty_dict = {}
    for n in inputs:
        num = inputs.count(n)
        empty_dict.update({n: num})
    print(empty_dict)


# return {word:word.count(word) for word in words}
inputs = "google.com"
print(count_string(inputs))
