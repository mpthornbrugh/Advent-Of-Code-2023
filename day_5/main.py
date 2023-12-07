from inputs import *


def get_seed_numbers(seed_lines):
    seed_line = seed_lines[0]
    seed_line = seed_line.replace('seeds: ', '')
    seed_numbers = seed_line.split(' ')
    seed_numbers = [int(seed_number) for seed_number in seed_numbers if seed_number != '']
    # Part 2: Convert every pair of 2 seed numbers into a range where the
    #   first number is the start and the second is the range
    #   e.g. [1, 3, 5, 4] -> [1, 2, 3, 5, 6, 7, 8]
    new_seed_numbers = []
    for i in range(0, len(seed_numbers), 2):
        start = seed_numbers[i]
        end = seed_numbers[i + 1] + start
        new_seed_numbers += list(range(start, end + 1))
    return seed_numbers


def get_seed_number_ranges(seed_lines):
    seed_line = seed_lines[0]
    seed_line = seed_line.replace('seeds: ', '')
    seed_numbers = seed_line.split(' ')
    seed_numbers = [int(seed_number) for seed_number in seed_numbers if seed_number != '']
    # Part 2: Convert every pair of 2 seed numbers into a range where the
    #   first number is the start and the second is the range
    #   e.g. [1, 3, 5, 4] -> [1, 2, 3, 5, 6, 7, 8]
    seed_ranges = []
    for i in range(0, len(seed_numbers), 2):
        start = seed_numbers[i]
        end = seed_numbers[i + 1] + start
        seed_ranges.append({
            'start': start,
            'end': end,
        })
    # Sort by start
    seed_ranges = sorted(seed_ranges, key=lambda x: x['start'])
    return seed_ranges


def create_conversion_dict(lines):
    result_conversions = []
    for line in lines:
        dest_range_start, src_range_start, range_length = line.split(' ')
        dest_range_start = int(dest_range_start)
        src_range_start = int(src_range_start)
        range_length = int(range_length)
        result_conversions.append({
            'start': src_range_start,
            'end': src_range_start + range_length,
            'conversion': src_range_start - dest_range_start,
        })
    # Sort by start
    result_conversions = sorted(result_conversions, key=lambda x: x['start'])
    return result_conversions


def convert_number(number, conversions):
    for conversion in conversions:
        if conversion['start'] <= number <= conversion['end']:
            return number - conversion['conversion']
    return number


def convert_ranges(ranges, conversions):
    """
    Example:
        ranges: [{'start': 79, 'end': 93}, {'start': 55, 'end': 68}, {'start': 102, 'end': 105}]
        conversions: [{'start': 98, 'end': 100, 'conversion': 48}, {'start': 50, 'end': 90, 'conversion': -2}]
        result: [
            {'start': 77, 'end': 88}, {'start': 91, 'end': 93}, {'start': 53, 'end': 66}, {'start': 102, 'end': 105}
        ]
    """
    result = []

    ranges_to_convert = []
    # Find any ranges that are not within any conversion range
    for range_to_convert in ranges:
        overlaps = []
        for conversion in conversions:
            # If the range if fully within the conversion
            if (
                conversion['start'] <= range_to_convert['start'] <= conversion['end']
            ) and (
                conversion['start'] <= range_to_convert['end'] <= conversion['end']
            ):
                overlaps.append({
                    'start': range_to_convert['start'],
                    'end': range_to_convert['end'],
                    'conversion': conversion['conversion'],
                })
                break
            else:
                # Otherwise check if it still overlaps on one side
                # If the conversion starts before the range, but ends before the range
                if conversion['start'] <= range_to_convert['start'] <= conversion['end']:
                    overlaps.append({
                        'start': range_to_convert['start'],
                        'end': conversion['end'],
                        'conversion': conversion['conversion'],
                    })
                # If the conversion starts within the range, but ends after the range
                elif conversion['start'] <= range_to_convert['end'] <= conversion['end']:
                    overlaps.append({
                        'start': conversion['start'],
                        'end': range_to_convert['end'],
                        'conversion': conversion['conversion'],
                    })
                # If the conversion starts and ends within the range
                elif (
                    range_to_convert['start'] <= conversion['start'] <= range_to_convert['end']
                ) and (
                    range_to_convert['start'] <= conversion['end'] <= range_to_convert['end']
                ):
                    overlaps.append({
                        'start': conversion['start'],
                        'end': conversion['end'],
                        'conversion': conversion['conversion'],
                    })
        # If there are no overlaps, add the range to the result
        if len(overlaps) == 0:
            result.append(range_to_convert)
        else:
            # Sort overlaps by start
            overlaps = sorted(overlaps, key=lambda x: x['start'])
            # If there are more than 1 overlaps, check if there are gaps between them
            if len(overlaps) > 1:
                for i in range(1, len(overlaps)):
                    # If there is a gap, add the range between the overlaps to the result
                    if overlaps[i]['start'] > overlaps[i - 1]['end']:
                        result.append({
                            'start': overlaps[i - 1]['end'] + 1,
                            'end': overlaps[i]['start'] - 1,
                        })
            # Determine min and max of overlaps
            min_overlap = overlaps[0]['start']
            max_overlap = overlaps[0]['end']
            for overlap in overlaps:
                # Calculate the min and max overlap
                if overlap['start'] < min_overlap:
                    min_overlap = overlap['start']
                if overlap['end'] > max_overlap:
                    max_overlap = overlap['end']
                # Apply the conversion to the overlapped area
                result.append({
                    'start': overlap['start'] - overlap['conversion'],
                    'end': overlap['end'] - overlap['conversion'],
                })
            # If the min overlap is more than the range start we need to add that to the result
            if min_overlap > range_to_convert['start']:
                result.append({
                    'start': range_to_convert['start'],
                    'end': min_overlap - 1,
                })
            # If the max overlap is less than the range end we need to add that to the result
            if max_overlap < range_to_convert['end']:
                result.append({
                    'start': max_overlap + 1,
                    'end': range_to_convert['end'],
                })
    # Sort result by start
    result = sorted(result, key=lambda x: x['start'])
    return result


def create_map_from_lines(lines):
    result_map = {}
    for line in lines:
        dest_range_start, src_range_start, range_length = line.split(' ')
        dest_range_start = int(dest_range_start)
        src_range_start = int(src_range_start)
        range_length = int(range_length)
        for i in range(range_length):
            result_map[src_range_start + i] = dest_range_start + i
    return result_map


def get_min_location_from_ranges(ranges):
    return ranges[0]['start']


def calculate(input_string):
    lines = input_string.split('\n')
    seed_lines = []
    seed_to_soil_lines = []
    soil_to_fertilizer_lines = []
    fertilizer_to_water_lines = []
    water_to_light_lines = []
    light_to_temperature_lines = []
    temperature_to_humidity_lines = []
    humidity_to_location_lines = []
    stage = 0
    for line in lines:
        if line == "":
            stage += 1
            continue
        if stage == 0:
            seed_lines.append(line)
        elif stage == 1:
            seed_to_soil_lines.append(line)
        elif stage == 2:
            soil_to_fertilizer_lines.append(line)
        elif stage == 3:
            fertilizer_to_water_lines.append(line)
        elif stage == 4:
            water_to_light_lines.append(line)
        elif stage == 5:
            light_to_temperature_lines.append(line)
        elif stage == 6:
            temperature_to_humidity_lines.append(line)
        elif stage == 7:
            humidity_to_location_lines.append(line)
    seed_to_soil_conversions = create_conversion_dict(seed_to_soil_lines[1:])
    soil_to_fertilizer_conversions = create_conversion_dict(soil_to_fertilizer_lines[1:])
    fertilizer_to_water_conversions = create_conversion_dict(fertilizer_to_water_lines[1:])
    water_to_light_conversions = create_conversion_dict(water_to_light_lines[1:])
    light_to_temperature_conversions = create_conversion_dict(light_to_temperature_lines[1:])
    temperature_to_humidity_conversions = create_conversion_dict(temperature_to_humidity_lines[1:])
    humidity_to_location_conversions = create_conversion_dict(humidity_to_location_lines[1:])
    min_location = None
    # Part 1
    # seed_numbers = get_seed_numbers(seed_lines)
    # for seed in seed_numbers:
    #     soil = convert_number(seed, seed_to_soil_conversions)
    #     fertilizer = convert_number(soil, soil_to_fertilizer_conversions)
    #     water = convert_number(fertilizer, fertilizer_to_water_conversions)
    #     light = convert_number(water, water_to_light_conversions)
    #     temperature = convert_number(light, light_to_temperature_conversions)
    #     humidity = convert_number(temperature, temperature_to_humidity_conversions)
    #     location = convert_number(humidity, humidity_to_location_conversions)
    #     if min_location is None or location < min_location:
    #         min_location = location
    #     print(f"Seed {seed}, soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temperature}, humidity {humidity}, location {location}")
    # Part 2
    seed_ranges = get_seed_number_ranges(seed_lines)
    soil_ranges = convert_ranges(seed_ranges, seed_to_soil_conversions)
    fertilizer_ranges = convert_ranges(soil_ranges, soil_to_fertilizer_conversions)
    water_ranges = convert_ranges(fertilizer_ranges, fertilizer_to_water_conversions)
    light_ranges = convert_ranges(water_ranges, water_to_light_conversions)
    temperature_ranges = convert_ranges(light_ranges, light_to_temperature_conversions)
    humidity_ranges = convert_ranges(temperature_ranges, temperature_to_humidity_conversions)
    location_ranges = convert_ranges(humidity_ranges, humidity_to_location_conversions)
    min_location = get_min_location_from_ranges(location_ranges)
    print(f"Min location: {min_location}")


if __name__ == '__main__':
    # calculate(example_input)
    calculate(puzzle_input)
