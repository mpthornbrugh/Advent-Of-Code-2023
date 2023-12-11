from inputs import *
import pandas as pd
import numpy as np


def is_unique(line_numbers):
    if len(line_numbers) <= 1:
        return True
    a = line_numbers.to_numpy()
    return (a[0] == a).all()


def calculate_line(line_numbers):
    line_numbers = pd.Series(line_numbers)
    if is_unique(line_numbers):
        return line_numbers.iloc[0]
    diffs = line_numbers.diff().dropna()
    # Part 1
    # add_value = calculate_line(diffs)
    # return line_numbers.iloc[-1] + add_value
    # Part 2
    sub_value = calculate_line(diffs)
    return line_numbers.iloc[0] - sub_value


def calculate(input_string):
    lines = input_string.split("\n")
    total = 0
    for line in lines:
        line_numbers = line.split(" ")
        line_numbers = [int(x) for x in line_numbers if x != ""]
        if len(line_numbers) == 0:
            continue
        value = calculate_line(line_numbers)
        # print(value)
        total += value
    print(total)


if __name__ == "__main__":
    # calculate(example_input)
    calculate(puzzle_input)
