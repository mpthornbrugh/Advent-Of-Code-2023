from inputs import *


def print_grid(grid):
    for line in grid:
        print("".join(line))


def calculate_galaxy_locations(lines, columns_with_galaxies, rows_with_galaxies):
    expansion_factor = 1000000
    galaxy_locations = []
    # While looping through the lines if a row or column has no galaxy then *1000000 that row/column
    current_row = 0
    for row_index, row in enumerate(lines):
        current_col = 0
        if row_index not in rows_with_galaxies:
            current_row += expansion_factor
        else:
            for column_index, column in enumerate(row):
                if column == "#":
                    galaxy_locations.append((current_row, current_col))
                # print(current_row, current_col, column)
                current_col += 1
                if column_index not in columns_with_galaxies:
                    current_col += expansion_factor - 1
            current_row += 1
    return galaxy_locations


def construct_galaxy_grid(lines, columns_with_galaxies, rows_with_galaxies, start_rows, start_columns):
    # Determine the expanded rows and columns
    expanded_rows = start_rows + (start_rows - len(rows_with_galaxies))
    expanded_columns = start_columns + (start_columns - len(columns_with_galaxies))
    galaxy_locations = []
    # While looping through the lines if a row or column has no galaxy then double that row/column
    result_grid = []
    for row_index, row in enumerate(lines):
        if row_index not in rows_with_galaxies:
            result_grid.append(["." for _ in range(expanded_columns)])
            result_grid.append(["." for _ in range(expanded_columns)])
        else:
            result_grid.append([])
            for column_index, column in enumerate(row):
                result_grid[-1].append(column)
                if column == "#":
                    galaxy_locations.append((len(result_grid) - 1, len(result_grid[-1]) - 1))
                if column_index not in columns_with_galaxies:
                    result_grid[-1].append(".")
    return result_grid, galaxy_locations


def calculate(input_string):
    columns_with_galaxies = {}
    rows_with_galaxies = {}
    lines = input_string.split("\n")
    start_rows = len(lines)
    start_columns = len(lines[0])
    # Determine which columns and rows have galaxies
    for row_index, row in enumerate(lines):
        for column_index, column in enumerate(row):
            if column == "#":
                columns_with_galaxies[column_index] = True
                rows_with_galaxies[row_index] = True
    # Construct the expanded galaxy
    # Part 1
    # galaxy_grid, galaxy_locations = construct_galaxy_grid(
    #     lines, columns_with_galaxies, rows_with_galaxies, start_rows, start_columns
    # )
    galaxy_locations = calculate_galaxy_locations(lines, columns_with_galaxies, rows_with_galaxies)
    # print_grid(galaxy_grid)
    total_distance = 0
    # For every pair of galaxies calculate the distance
    for index, galaxy in enumerate(galaxy_locations):
        for other_galaxy in galaxy_locations[index + 1:]:
            total_distance += abs(galaxy[0] - other_galaxy[0]) + abs(galaxy[1] - other_galaxy[1])
    print(total_distance)


if __name__ == "__main__":
    # calculate(example_input)
    calculate(puzzle_input)
