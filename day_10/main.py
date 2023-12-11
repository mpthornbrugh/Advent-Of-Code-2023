import copy
from inputs import *


def print_grid(grid):
    for line in grid:
        print("".join(line))


def find_steps_from_start_to_start(grid, start_line, start_char):
    spaces_to_check = []
    grid_rows = len(grid)
    grid_cols = len(grid[0])
    cleaned_grid = []
    for _line in grid:
        cleaned_grid.append(["." for _char in range(grid_cols)])
    # Initialize the spaces to check with the starting space
    if start_line > 0 and grid[start_line - 1][start_char] in ("|", "7", "F"):
        spaces_to_check.append((start_line - 1, start_char, "U"))
    if start_line < grid_rows - 1 and grid[start_line + 1][start_char] in (
            "|", "J", "L",
    ):
        spaces_to_check.append((start_line + 1, start_char, "D"))
    if start_char > 0 and grid[start_line][start_char - 1] in ("-", "L", "F"):
        spaces_to_check.append((start_line, start_char - 1, "L"))
    if start_char < grid_rows - 1 and grid[start_line][start_char + 1] in (
            "-", "7", "J",
    ):
        spaces_to_check.append((start_line, start_char + 1, "R"))
    steps_until_back_at_start = 0
    while steps_until_back_at_start < 9999999:
        new_spaces_to_check = []
        steps_until_back_at_start += 1
        for space in spaces_to_check:
            y = space[0]
            x = space[1]
            label = grid[y][x]
            cleaned_grid[y][x] = label
            if label == "S":
                # Replace the "S" in the cleaned grid with the correct pipe piece
                connection_top = False
                connection_bottom = False
                connection_left = False
                connection_right = False
                if y > 0 and grid[y - 1][x] in ("|", "7", "F"):
                    connection_top = True
                if y < grid_rows - 1 and grid[y + 1][x] in ("|", "J", "L"):
                    connection_bottom = True
                if x > 0 and grid[y][x - 1] in ("-", "L", "F"):
                    connection_left = True
                if x < grid_cols - 1 and grid[y][x + 1] in ("-", "7", "J"):
                    connection_right = True
                if connection_top and connection_bottom:
                    cleaned_grid[y][x] = "|"
                elif connection_left and connection_right:
                    cleaned_grid[y][x] = "-"
                elif connection_top and connection_right:
                    cleaned_grid[y][x] = "L"
                elif connection_top and connection_left:
                    cleaned_grid[y][x] = "J"
                elif connection_bottom and connection_right:
                    cleaned_grid[y][x] = "F"
                elif connection_bottom and connection_left:
                    cleaned_grid[y][x] = "7"
                else:
                    raise Exception("Invalid start space")
                return steps_until_back_at_start, cleaned_grid
            space_direction = space[2]
            if label == ".":
                continue
            if space_direction == "U":
                # One more space up
                if label == "|":
                    if y > 0:
                        new_spaces_to_check.append(
                            (y - 1, x, "U")
                        )
                # Going to the left
                if label == "7":
                    if x > 0:
                        new_spaces_to_check.append(
                            (y, x - 1, "L")
                        )
                # Going to the right
                if label == "F":
                    if x < grid_cols - 1:
                        new_spaces_to_check.append(
                            (y, x + 1, "R")
                        )
            if space_direction == "D":
                # One more space down
                if label == "|":
                    if y < grid_rows - 1:
                        new_spaces_to_check.append(
                            (y + 1, x, "D")
                        )
                # Going to the left
                if label == "J":
                    if x > 0:
                        new_spaces_to_check.append(
                            (y, x - 1, "L")
                        )
                # Going to the right
                if label == "L":
                    if x < grid_cols - 1:
                        new_spaces_to_check.append(
                            (y, x + 1, "R")
                        )
            if space_direction == "L":
                # One more space left
                if label == "-":
                    if x > 0:
                        new_spaces_to_check.append(
                            (y, x - 1, "L")
                        )
                # Going up
                if label == "L":
                    if y > 0:
                        new_spaces_to_check.append(
                            (y - 1, x, "U")
                        )
                # Going down
                if label == "F":
                    if y < grid_rows - 1:
                        new_spaces_to_check.append(
                            (y + 1, x, "D")
                        )
            if space_direction == "R":
                # One more space right
                if label == "-":
                    if x < grid_cols - 1:
                        new_spaces_to_check.append(
                            (y, x + 1, "R")
                        )
                # Going up
                if label == "J":
                    if y > 0:
                        new_spaces_to_check.append(
                            (y - 1, x, "U")
                        )
                # Going down
                if label == "7":
                    if y < grid_rows - 1:
                        new_spaces_to_check.append(
                            (y + 1, x, "D")
                        )
        spaces_to_check = new_spaces_to_check


def calculate_enclosed_tiles(grid):
    note_taking_grid = copy.deepcopy(grid)
    enclosed_count = 0
    for row_num, row in enumerate(grid):
        enclosed = False
        # Determine the last column that has a non . character
        max_col = 0
        for col_num, col in enumerate(row):
            if col != ".":
                max_col = col_num
        # Loop through the row forwards
        for col_num, col in enumerate(row):
            if col_num > max_col:
                continue
            if col == ".":
                if enclosed:
                    note_taking_grid[row_num][col_num] = "I"
                    enclosed_count += 1
            else:
                # If the current space is a pipe that is facing north then flip the enclosed flag
                if col in ("|", "J", "L"):
                    enclosed = not enclosed
    # print_grid(note_taking_grid)
    return enclosed_count


def calculate(input_string):
    grid = []
    lines = input_string.split("\n")
    start_line = 0
    start_char = 0
    for line_num, line in enumerate(lines):
        grid.append([])
        for char_num, char in enumerate(line):
            grid[line_num].append(char)
            if char == "S":
                start_line = line_num
                start_char = char_num
    steps_through_loop, cleaned_grid = find_steps_from_start_to_start(grid, start_line, start_char)
    # print_grid(cleaned_grid)
    # print("-------------------------------")
    # Part 1
    # print(int(steps_through_loop / 2))
    # Part 2
    enclosed_tiles = calculate_enclosed_tiles(cleaned_grid)
    print(enclosed_tiles)


if __name__ == "__main__":
    # calculate(example_input)
    # calculate(example_input_2)
    # calculate(example_input_3)
    # calculate(example_input_4)
    # calculate(example_input_5)
    calculate(puzzle_input)
