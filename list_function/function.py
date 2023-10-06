def largest(number):
    largest = 0
    for nums in number:
        if nums > largest:
            largest = nums
    return largest


# numbers = [1, 3, 5, 6, 7]
# print(largest(numbers))

def reverse(numbers):
    num = numbers[::-1]

    return num


# number = [1, 2, 3, 4]
# print(reverse(number))

def check_element(numbers, element):
    for num in numbers:
        if element == numbers:
            return True
        else:
            return False


def oddlyplaced(numbers):
    num = len(numbers)
    numb = numbers[1:num:2]
    return numb


# number = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# print(oddlyplaced(number))


def evenly_placed(numbers):
    num = len(numbers)
    numb = numbers[0:num:2]
    return numb


# number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(evenly_placed(number))


def running_total(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum


def palindrome(numbers):
    if str(numbers) == str(numbers)[::-1]:
        return True
    else:
        return False


def sum_for_loop(number):
    sum = 0
    for num in number:
        sum += num
    return sum


def sums_while_loop(numbers):
    length = len(numbers)
    num = 0
    sums = 0
    while num < length:
        sums += numbers
    return length


def concatenates(num, letters):
    total = len(num)
    num = num[0:total:1]
    nums = letters[0:total:1]
    return num + nums


def combine_elements(letters, num, ):
    totall = len(num) + len(letters)
    count = 0
    counter = 0
    while count < len(num):
        total = letters[count] + "," + num[count]
        count += 1
        print(total)
        # return total


def convert(numberss):
    suumss = list(numberss)
    print(suumss)


letter = ['a', 'b', 'c', 'd', 'e']
number = ['1', '2', '3', '4', '5']
print(combine_elements(letter, number))
