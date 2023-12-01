import sys

def extract_calibration_value(cal_str: str) -> int:
    left_window = 0
    right_window = len(cal_str) - 1
    left_value = None
    right_value = None

    while left_value is None and left_window < len(cal_str):
        if cal_str[left_window].isdigit():
            left_value = cal_str[left_window]
        else:
            left_window = left_window + 1

    while right_value is None and right_window >= 0:
        if cal_str[right_window].isdigit():
            right_value = cal_str[right_window]
        else:
            right_window = right_window - 1
    
    # Am I going to have to worry about none checks?
    # Doesn't look like it. It appears every row has a number.
    return int(left_value + right_value)

def parse_input_data(input_data: list[str]) -> int:
    total = 0
    for val in input_data:
        total += extract_calibration_value(val)
    return total

if __name__ == "__main__":
    file_name = sys.argv[1]
    
    input_data = []

    with open(file_name) as input_file:
        input_data = input_file.read().splitlines()

    answer = parse_input_data(input_data)

    print(answer)