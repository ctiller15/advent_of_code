import sys

# What counts as a symbol?
# Incorrect answer: 503939
# Incorrect answer: 543212
# Correct answer for part 1 - not gonna tell!

# Come up with a more exhaustive list before submitting solution.
symbols = ["*", "#", "+", "$", "!", "@", "%", "^", "&", "(", ")", "/", "=", "-"]

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

def checkSurroundingValues(prev_row: list[str] | None, curr_row: list[str], next_row: list[str] | None, column: int, row_num: int):
    numbers_with_cols = []

    if prev_row:
        numbers_with_cols += check_row_for_numbers(prev_row, column, row_num - 1)

    numbers_with_cols += check_row_for_numbers(curr_row, column, row_num)

    if next_row:
        numbers_with_cols += check_row_for_numbers(next_row, column, row_num + 1)

    return numbers_with_cols

def main(input: list[str]):
    # Loop through every single row.
    all_valid_values = []
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] in symbols:
                previous_row = input[i - 1] if i > 0 else None
                current_row = input[i]
                next_row = input[i + 1] if i < len(input) else None
                value_to_add = checkSurroundingValues(previous_row, current_row, next_row, j, i)
                all_valid_values += value_to_add
                # Then check everything within one character of that symbol.

    dupes_removed = [dict(t) for t in {tuple(d.items()) for d in all_valid_values}]
    print(dupes_removed)
    print(sum([item["value"] for item in dupes_removed]))

if __name__ == '__main__':
    file_name = sys.argv[1]

    input_data: list[str] = []

    with open(file_name) as input_file:
        input_data = input_file.read().splitlines()

    main(input_data)