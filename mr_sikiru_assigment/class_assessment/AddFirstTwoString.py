# def swapFirstTwoCharacter(first_word: str, second_word: str):
#     final_string = ""
#     firstTwo = first_word[0]
#     firstTwos = first_word[1]
#
#     secondTwo = second_word[0]
#     secondTwos = second_word[1]
#
#     other_letters1 = slice(2, len(first_word) + 1)
#     other_letters2 = slice(2, len(second_word) + 1)
#
#     final_string += secondTwo
#     final_string += secondTwos
#     final_string += first_word[other_letters1]
#     final_string += " "
#     final_string += firstTwo
#     final_string += firstTwos
#     final_string += second_word[other_letters2]
#
#     return final_string
def swapFirstTwoCharacter(first_word: str, second_word: str):
    final_string = ""
    sliced_index = slice(0,2)
    final_string += second_word[sliced_index]

    for letter in range(2, len(first_word)):
        final_string += first_word[letter]
        print(final_string)
    for letter in range(2, len(second_word)):
        final_string += second_word[letter]
        print(final_string)

        return final_string


print(swapFirstTwoCharacter("abc", "xyz"))
