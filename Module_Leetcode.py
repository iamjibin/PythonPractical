def palindrome(num):
    y = str(num)
    length = len(y)
    output = ""
    for i in reversed(range(0, length)):
        output += y[i]
    print(output)
    if y == output:
        return "Palindrome"
    else:
        return "Not palindrome"


def roman_to_int(roman):
    roman_int_converter = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }
    output = 0
    length = len(roman)
    print(length)
    temp = ""
    for i in range(length):
        if i < length - 1:
            temp = roman[i + 1]
        if roman[i] + temp in ["IV", "IX", "XL", "XC", "CD", "CM"]:
            output += roman_int_converter.get(roman[i] + temp)
            print(f'{roman[i] + temp} : {roman_int_converter.get(roman[i] + temp)}')
        elif roman[i - 1] + roman[i] in ["IV", "IX", "XL", "XC", "CD", "CM"] and i != 0:
            continue
        else:
            output += roman_int_converter.get(roman[i])
            print(f'{roman[i]} : {roman_int_converter.get(roman[i])}')
    return output


def largest_num(nums):
    largest = 0
    for number in nums:
        if number > largest:
            largest = number
    return largest


def find_index(nums, target):
    length = len(nums)
    print(length)
    temp = 0
    index = []
    output = ""
    for i in range(0, length):
        temp = nums[i]
        for j in range(i + 1, length):
            if i != j and temp + nums[j] == target:
                index.extend([i, j])
                # index.append(j)
    return index


def valid_parenthesis(s):
    d = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for i in s:
        if i in d:
            stack.append(i)
        elif len(stack) == 0 or d[stack.pop()] != i:
            return 0
    return len(stack) == 0
