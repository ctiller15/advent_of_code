import sys

def extractNumberFromRow(row: list[str], start_col: int, row_num: int):
    initial_number = row[start_col]
    ind = start_col
    final_start = start_col
    
    # Traverse backwards
    while ind > 0 and row[ind - 1].isdigit():
        initial_number = row[ind - 1] + initial_number
        final_start = ind - 1
        ind = ind - 1

    # Traverse forwards
    ind = start_col
    while ind < len(row) - 1 and row[ind + 1].isdigit():
        initial_number = initial_number + row[ind + 1]
        ind = ind + 1

    extracted_value = int(initial_number)
    extracted_column = final_start
    return { "value": extracted_value, "col": extracted_column, "row": row_num}
    
def check_row_for_numbers(row: list[str], col: int, row_num):
    number_arrs = []
    if col > 0:
        if str(row[col - 1]).isdigit():
            number_element = extractNumberFromRow(row, col - 1, row_num)
            number_arrs.append(number_element)

    if str(row[col]).isdigit():
        number_element = extractNumberFromRow(row, col, row_num)
        number_arrs.append(number_element)

    if col < len(row) - 1:
        if str(row[col + 1]).isdigit():
            number_element = extractNumberFromRow(row, col + 1, row_num)
            number_arrs.append(number_element)

    return number_arrs

def is_gear(prev_row: list[str] | None, curr_row: list[str], next_row: list[str] | None, column: int):
    print(column)
    # Account for edges at both top and bottom.
    # No gears are near edges in input data. Disregard.
    number_count = 0

    rows: list[list[str]] = [
        prev_row[column - 1 : column + 2], 
        curr_row[column - 1 : column + 2], 
        next_row[column - 1 : column + 2]
    ]

    for row in rows:
        prev_is_digit = False
        for i in range(len(row)):
            if row[i].isdigit() and not prev_is_digit:
                number_count += 1
                prev_is_digit = True
            elif not row[i].isdigit() and prev_is_digit:
                prev_is_digit = False

    print(number_count)

    return number_count == 2 

def calculate_gear_ratio(gear_values: list[dict]):
    if len(gear_values) == 0:
        return 0

    product = 1
    
    for item in gear_values:
        product *= item["value"]

    return product

def checkSurroundingValues(prev_row: list[str] | None, curr_row: list[str], next_row: list[str] | None, column: int, row_num: int):
    print('checking surrounding vals!')
    gear_values = []

    if is_gear(prev_row, curr_row, next_row, column):
        print(f"Found a gear at {row_num}, {column}")
        if prev_row:
            gear_values += check_row_for_numbers(prev_row, column, row_num - 1)

        gear_values += check_row_for_numbers(curr_row, column, row_num)

        if next_row:
            gear_values += check_row_for_numbers(next_row, column, row_num + 1)
    
    dupes_removed = [dict(t) for t in {tuple(d.items()) for d in gear_values}]

    return calculate_gear_ratio(dupes_removed)

def main(input: list[str]):
    # Loop through every single row.
    gear_ratio_sum = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "*":
                previous_row = input[i - 1] if i > 0 else None
                current_row = input[i]
                next_row = input[i + 1] if i < len(input) else None
                value_to_add = checkSurroundingValues(previous_row, current_row, next_row, j, i)
                gear_ratio_sum += value_to_add

    print(gear_ratio_sum)

if __name__ == '__main__':
    file_name = sys.argv[1]

    input_data: list[str] = []

    with open(file_name) as input_file:
        input_data = input_file.read().splitlines()

    main(input_data)