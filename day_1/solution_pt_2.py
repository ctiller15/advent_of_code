import sys

numbers_list = [
    {
        "name": "one",
        "value": "1"
    },
    {
        "name": "two",
        "value": "2"
    },
    {
        "name": "three",
        "value": "3"
    },
    {
        "name": "four",
        "value": "4"
    },
    {
        "name": "five",
        "value": "5"
    },
    {
        "name": "six",
        "value": "6"
    },
    {
        "name": "seven",
        "value": "7"
    },
    {
        "name": "eight",
        "value": "8"
    },
    {
        "name": "nine",
        "value": "9"
    }
]

def check_letters_left(cal_str_slice: str) -> int | None:
    ind = 0
    numbers_remaining = [num for num in numbers_list]
    while ind <= 5 and ind < len(cal_str_slice):
        numbers_remaining = [num for num in numbers_remaining if num["name"][ind] == cal_str_slice[ind]]
        ind = ind + 1

        if len(numbers_remaining) == 0:
            return None

        success_candidates = [num for num in numbers_remaining if len(num["name"]) == ind]

        if len(success_candidates) > 0:
            return success_candidates[0]["value"]

def check_letters_right(cal_str_slice: str) -> int | None:
    digits_traversed = 0
    ind = len(cal_str_slice) - 1
    numbers_remaining = [num for num in numbers_list]
    while ind >= 0:
        # Check if value matches calibration string at same index.
        numbers_remaining = [num for num in numbers_remaining if num["name"][ind - (len(cal_str_slice) - len(num["name"]))] == cal_str_slice[ind]]
        ind = ind - 1
        digits_traversed = digits_traversed + 1

        if len(numbers_remaining) == 0:
            return None

        success_candidates = [num for num in numbers_remaining if len(num["name"]) == digits_traversed]
        if len(success_candidates) > 0:
            return success_candidates[0]["value"]
            
def extract_calibration_value(cal_str: str) -> int:
    left_window = 0
    right_window = len(cal_str) - 1
    left_value = None
    right_value = None

    while left_value is None and left_window < len(cal_str):
        if cal_str[left_window].isdigit():
            left_value = cal_str[left_window]
        else:
            left_value = check_letters_left(cal_str[left_window:])
            left_window = left_window + 1

    while right_value is None and right_window >= 0:
        if cal_str[right_window].isdigit():
            right_value = cal_str[right_window]
        else:
            right_value = check_letters_right(cal_str[:right_window + 1])
            right_window = right_window - 1
    
    print(int(left_value + right_value))
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