def convert_first_occurrence_to_a_character(inputs):
    first_letter = inputs[0]

    new_input = inputs.removeprefix(first_letter)

    for num in new_input[1:len(new_input)]:

        if num == first_letter:
            return first_letter + new_input.replace(num, "$")

        if first_letter not in new_input:
            return inputs


print(convert_first_occurrence_to_a_character("delidhted"))
