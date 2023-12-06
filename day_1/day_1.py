from inputs import *


word_number_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
word_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
reversed_word_numbers = ["eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin"]


def find_first_number(input_string):
    substring = ""
    for character in input_string:
        if character.isdigit():
            return character
        substring += character
        for word_number in word_numbers:
            if word_number in substring:
                return word_number_dict[word_number]


def find_last_number(input_string):
    substring = ""
    for character in input_string[::-1]:
        if character.isdigit():
            return character
        substring += character
        for word_number in reversed_word_numbers:
            if word_number in substring:
                return word_number_dict[word_number[::-1]][::-1]


def calculate_one_line(input_string):
    # Find the first and last digit and convert to a number
    first_number = find_first_number(input_string)
    last_number = find_last_number(input_string)
    full_number = int(str(first_number) + str(last_number))
    return full_number


def calculate(input_string):
    inputs = input_string.strip().split("\n")
    total = 0
    values = []
    for inp in inputs:
        value = calculate_one_line(inp)
        values.append(value)
        total += value
    print(values)
    print(total)


if __name__ == '__main__':
    # calculate(example_input)
    calculate(puzzle_input)
