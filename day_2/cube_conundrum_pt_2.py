#Largely the same, but we need the power of the sets of the cubes summed together.print
import sys
from typing import TypedDict

class ColorMap(TypedDict):
    red: int
    green: int
    blue: int

def calculate_single_game_power(game_str: str) -> int:
    game_split = game_str.split(":")
    game_results = game_split[1].split(";")

    color_maxima: ColorMap = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for game_result in game_results:
        cleaned_result = game_result.strip()
        color_counts = cleaned_result.split(",")
        for color_count in color_counts:
            [count, name] = color_count.strip().split(" ")

            if name in color_maxima and int(count) > int(color_maxima[name]):
                color_maxima[name] = int(count)


    return color_maxima["red"] * color_maxima["green"] * color_maxima["blue"]

def calculate_game_power_sum(
        input_data: list[str]
    ) -> int:
    total_id_sum = 0

    for game in input_data:
        total_id_sum = total_id_sum + calculate_single_game_power(game)

    return total_id_sum


if __name__ == '__main__':
    file_name = sys.argv[1]

    input_data = []

    with open(file_name) as input_file:
        input_data = input_file.read().splitlines()

    power_sum = calculate_game_power_sum(input_data)

    print(power_sum) 