from inputs import *


def read_input_to_2d_array(input_string):
    return [list(line) for line in input_string.splitlines()]


def number_location_has_surrounding_symbols(number_location, symbol_locations):
    # Search the row above the number
    if number_location['row'] - 1 in symbol_locations:
        for i in range(number_location['start'] - 1, number_location['end'] + 2):
            if i in symbol_locations[number_location['row'] - 1]:
                return number_location['row'] - 1, i
    # Search before and after the number
    if number_location['row'] in symbol_locations:
        if number_location['start'] - 1 in symbol_locations[number_location['row']]:
            return number_location['row'], number_location['start'] - 1
        if number_location['end'] + 1 in symbol_locations[number_location['row']]:
            return number_location['row'], number_location['end'] + 1
    # Search the row below the number
    if number_location['row'] + 1 in symbol_locations:
        for i in range(number_location['start'] - 1, number_location['end'] + 2):
            if i in symbol_locations[number_location['row'] + 1]:
                return number_location['row'] + 1, i
    return -1, -1


def get_number_from_location(start, end, row, input_array):
    number = ""
    for i in range(start, end + 1):
        number += input_array[row][i]
    return int(number)


def calculate(input_string):
    input_array = read_input_to_2d_array(input_string)
    valid_numbers = []
    valid_numbers_2 = []
    # Create a list of all the number locations and a dictionary of all the symbol locations
    # Symbol locations will look like: {"row1": {"col3": True}, "row2": {"col1": True, "col2": True}}
    symbol_locations = {}
    gear_locations = {}
    number_locations = []
    for row_number, row in enumerate(input_array):
        number_start = None
        number_end = None
        for char_num, char in enumerate(row):
            if char == ".":
                if number_start is not None:
                    number_locations.append({
                        "start": number_start,
                        "end": number_end,
                        "row": row_number,
                        "number": get_number_from_location(number_start, number_end, row_number, input_array),
                    })
                    number_start = None
            elif char.isdigit():
                if number_start is None:
                    number_start = char_num
                number_end = char_num
            else:
                if number_start is not None:
                    number_locations.append({
                        "start": number_start,
                        "end": number_end,
                        "row": row_number,
                        "number": get_number_from_location(number_start, number_end, row_number, input_array),
                    })
                    number_start = None
                if char == "*":
                    if row_number not in gear_locations:
                        gear_locations[row_number] = {}
                    gear_locations[row_number][char_num] = True
                if row_number not in symbol_locations:
                    symbol_locations[row_number] = {}
                symbol_locations[row_number][char_num] = True
        if number_start is not None:
            number_locations.append({
                "start": number_start,
                "end": number_end,
                "row": row_number,
                "number": get_number_from_location(number_start, number_end, row_number, input_array),
            })
    # Part 2
    # Find out any gear symbols that have exactly 2 numbers next to them
    gear_adj_numbers = {}
    for number_location in number_locations:
        row, col = number_location_has_surrounding_symbols(number_location, gear_locations)
        if row > -1:
            if row not in gear_adj_numbers:
                gear_adj_numbers[row] = {}
            if col not in gear_adj_numbers[row]:
                gear_adj_numbers[row][col] = []
            gear_adj_numbers[row][col].append(number_location['number'])
    # Loop through the gear_adj_numbers and find the ones that have exactly 2 numbers.
    #   Multiply the numbers together and add them to the list of valid numbers 2
    for row in gear_adj_numbers:
        for col in gear_adj_numbers[row]:
            if len(gear_adj_numbers[row][col]) == 2:
                valid_numbers_2.append(gear_adj_numbers[row][col][0] * gear_adj_numbers[row][col][1])
    print(valid_numbers_2)
    print(sum(valid_numbers_2))

    # Part 1
    # For each number_location determine if there is a surrounding symbol
    #   If the number is surrounded by symbols then add it to the list of valid numbers
    for number_location in number_locations:
        row, col = number_location_has_surrounding_symbols(number_location, gear_locations)
        if row > -1:
            valid_numbers.append(number_location["number"])
    # print(valid_numbers)
    # print(sum(valid_numbers))


if __name__ == "__main__":
    calculate(puzzle_input)
