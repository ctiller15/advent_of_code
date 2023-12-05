import sys
# TODO: Revisit day 5 pt 2.

def parse_to_map(input: str):
    return [[int(num) for num in val.split()] for val in[row for row in input.split(":")[1].strip().split("\n")]]

def handle_seed_mappings(seeds: list[int], data_mapping):
    mapped_seeds = []
    for seed in seeds:
        mapped_seeds.append(handle_seed_mapping(seed, data_mapping))

    return mapped_seeds

def handle_seed_mapping(seed_number: int, data_mapping):
    mapped_value = seed_number
    found_mapping = False
    for s2s in data_mapping:
        if not found_mapping:

            if s2s[1] <= seed_number and (s2s[1] + s2s[2]) > seed_number:
                found_mapping = True
                mapped_value = seed_number + s2s[0] - s2s[1]
    
    return mapped_value

def part1(input_data: list[str]):
    data_map = {
        "seeds": {},
        "seed_to_soil": {},
        "soil_to_fertilizer": {},
        "fertilizer_to_water": {},
        "water_to_light": {},
        "light_to_temperature": {},
        "temperature_to_humidity": {},
        "humidity_to_location": {}
    }

    data_map["seeds"] = [int(item) for item in input_data[0].split(":")[1].strip().split()]

    data_maps = []

    data_maps.append(parse_to_map(input_data[1]))
    data_maps.append(parse_to_map(input_data[2]))
    data_maps.append(parse_to_map(input_data[3]))
    data_maps.append(parse_to_map(input_data[4]))
    data_maps.append(parse_to_map(input_data[5]))
    data_maps.append(parse_to_map(input_data[6]))
    data_maps.append(parse_to_map(input_data[7]))

    seed_map = data_map["seeds"]

    for data in data_maps:
        seed_map = handle_seed_mappings(seed_map, data)

    print(min(seed_map))

def calculate_ranges(seeds):
    ranges = []
    for i in range(0, len(seeds), 2):
        ranges.append({
            "start": seeds[i],
            "end": seeds[i] + seeds[i + 1]
        })

    # print(ranges)

    return ranges

def calculate_map_ranges(data_map):
    ranges = []
    for i in range(len(data_map)):
        ranges.append({
            "initial_state": {
                "start": data_map[i][1],
                "end": data_map[i][1] + data_map[i][2]
            },
            "end_state": {
                "start": data_map[i][0],
                "end": data_map[i][0] + data_map[i][2]
            }
        })

    return ranges

def compare_ranges(init, mapping):
    print("before...")
    print(init)
    print(mapping)

    # First, trim them down.
    for pairing in init:
        print(mapping)
        for maps in mapping:
            print("=====")
            print(maps)
            if maps["initial_state"]["start"] <= pairing["start"] and maps["initial_state"]["end"] >= pairing["end"]:
                # Trim it down.
                start_distance = pairing["start"] - maps["initial_state"]["start"]
                end_distance = maps["initial_state"]["end"] - pairing["end"] 
                
                prev_slice = {
                    "initial_state": {
                        "start": maps["initial_state"]["start"],
                        "end": pairing["start"] - 1
                    },
                    "end_state": {
                        "start": maps["end_state"]["start"],
                        "end": pairing["start"] - 1 - start_distance
                    }
                }

                center_slice = {
                    "initial_state": {
                        "start": pairing["start"],
                        "end": pairing["end"]
                    },
                    "end_state": {
                        "start": pairing["start"] - start_distance,
                        "end": pairing["end"] - end_distance
                    }
                }

                next_slice = {
                    "initial_state": {
                        "start": pairing["end"] + 1,
                        "end": maps["initial_state"]["end"]
                    },
                    "end_state": {
                        "start": pairing["end"] + 1 - start_distance,
                        "end": pairing["end"]
                    }
                }

                mapping.append(prev_slice)

                mapping.append(center_slice)

                mapping.append(next_slice)

    print("after...")
    print(mapping)

    end_values = [val["end"] for val in init]

    print(end_values)
    trimmed_mappings_endings = [val for val in mapping if any(end_val >= val["initial_state"]["start"] for end_val in end_values)]
    print(trimmed_mappings_endings)
    
    start_values = [val["start"] for val in init]
    trimmed_mappings_starts = [val for val in trimmed_mappings_endings if any(start_val <= val["initial_state"]["end"] for start_val in start_values)]
    print(trimmed_mappings_starts)
    end_states = [range_end_state["end_state"] for range_end_state in trimmed_mappings_starts]
    print(end_states)
    if(len(end_states) == 0):
        return init
    return end_states

def part2(input_data):
    # Crazy thought.
    # Let's work backwards! Figure out what the lowest possible numbers are.
    # After, then work backwards through the maps to find the lowest value that is possible.
    data_map = {
        "seeds": {},
        "seed_to_soil": {},
        "soil_to_fertilizer": {},
        "fertilizer_to_water": {},
        "water_to_light": {},
        "light_to_temperature": {},
        "temperature_to_humidity": {},
        "humidity_to_location": {}
    }

    data_map["seeds"] = [int(item) for item in input_data[0].split(":")[1].strip().split()]

    data_maps = []

    data_maps.append(parse_to_map(input_data[1]))
    data_maps.append(parse_to_map(input_data[2]))
    data_maps.append(parse_to_map(input_data[3]))
    data_maps.append(parse_to_map(input_data[4]))
    data_maps.append(parse_to_map(input_data[5]))
    data_maps.append(parse_to_map(input_data[6]))
    data_maps.append(parse_to_map(input_data[7]))

    # We're mapping ranges.

    map_ranges = [calculate_map_ranges(data) for data in data_maps]

    init = calculate_ranges(data_map["seeds"])

    # map_range = calculate_map_ranges(data_maps[0])
    # print(init)

    # for item in map_ranges:
    #     print(item)

    next_state = init
    result = compare_ranges(init, map_ranges[0])
    print(result)
    # for next_range in map_ranges:
    #     next_state = compare_ranges(next_state, next_range)
    # resulting_range = compare_ranges(init, map_ranges[0])
    # print(next_state)




if __name__ == '__main__':
    input_file = sys.argv[1]

    input_data = []

    with open(input_file) as file:
        input_data = file.read().split("\n\n")
        # print(input_data)

    # part1(input_data)
    part2(input_data)