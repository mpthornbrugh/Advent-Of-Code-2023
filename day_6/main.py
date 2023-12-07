from inputs import *


def get_distance_travelled(time_held, total_time):
    return time_held * (total_time - time_held)


def calculate_winning_times(race):
    time_allowed, min_distance = race
    is_even_time = time_allowed % 2 == 0
    mid_time = time_allowed // 2
    max_distance = get_distance_travelled(mid_time, time_allowed)
    winning_times = 0
    if max_distance > min_distance:
        if is_even_time:
            winning_times = 1
        else:
            winning_times = 2
        calc_time = mid_time - 1
        calculated_distance = get_distance_travelled(calc_time, time_allowed)
        while calculated_distance > min_distance:
            winning_times += 2
            calc_time -= 1
            if calc_time == 0:
                break
            calculated_distance = get_distance_travelled(calc_time, time_allowed)
    return winning_times


def calculate(input_string):
    times, distances = input_string.split('\n')
    # Part 1
    # times = [int(x) for x in times.split(":")[-1].split() if x != '']
    # distances = [int(x) for x in distances.split(":")[-1].split() if x != '']
    # races = list(zip(times, distances))
    # Part 2
    race_time = int(times.split(":")[-1].replace(" ", ""))
    race_distance = int(distances.split(":")[-1].replace(" ", ""))
    races = [(race_time, race_distance)]
    total_winning_times = 1
    for race in races:
        print(race)
        winning_times = calculate_winning_times(race)
        print(winning_times)
        total_winning_times *= winning_times
    print(total_winning_times)


if __name__ == '__main__':
    calculate(example_input)
    # calculate(puzzle_input)
