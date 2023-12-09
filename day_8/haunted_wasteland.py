import sys

def part_1(input: list[str]):
    steps_count = 0
    current_step = "AAA"
    steps = input[0]
    mapping = input[2:]

    print(steps)

    print(mapping)
    letter_map = {}

    for row in mapping:
        row_split = row.split("=")
        mapping_key = row_split[0].strip()
        mapping_values = [value.strip() for value in row_split[1].replace("(", "").replace(")", "").split(",")]
        letter_map[mapping_key] = mapping_values

    print(letter_map)

    found = False
    while not found:
        current_step = letter_map[current_step][0 if steps[steps_count % len(steps)] == "L" else 1]
        steps_count += 1

        if current_step == "ZZZ":
            found = True
    
    print(steps_count)

def calculate_next_steps(letter_map, ):
    current_step = letter_map[current_step][0 if steps[step_counts % len(steps)] == "L" else 1]

def part_2(input: list[str]):
    initial_steps = []
    step_counts = 0

    steps = input[0]
    mapping = input[2:]
    multiples = []
    
    letter_map = {}

    for row in mapping:
        row_split = row.split("=")
        mapping_key = row_split[0].strip()
        mapping_values = [value.strip() for value in row_split[1].replace("(", "").replace(")", "").split(",")]
        letter_map[mapping_key] = mapping_values
        if mapping_key.endswith("A"):
            initial_steps.append(mapping_key)
            multiples.append(0)

    while not all(mult != 0 for mult in multiples):
        print(initial_steps)
        next_steps_temp: list[str] = []

        for test_step in initial_steps:
            next_step = letter_map[test_step][0 if steps[step_counts % len(steps)] == "L" else 1]
            next_steps_temp.append(next_step)

        initial_steps = next_steps_temp

        step_counts += 1
        for i in range(len(next_steps_temp)):
            if next_steps_temp[i].endswith("Z") and multiples[i] == 0:
                multiples[i] = step_counts

        # if all(ns.endswith("Z") for ns in next_steps_temp):
        #     found = True

    print(multiples)
    
    print(step_counts)

if __name__ == '__main__':
    file_name = sys.argv[1]

    input_lines = []

    with open(file_name) as input_file:
        input_lines = input_file.read().splitlines()

    # part_1(input_lines)
    part_2(input_lines)