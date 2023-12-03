import sys
from typing import TypedDict

class ColorMaximaMap(TypedDict):
    red: int
    green: int
    blue: int

def calculate_single_game_sum(game_str: str, colors: ColorMaximaMap):
    game_split = game_str.split(":")
    game_id = int(game_split[0].replace("Game ", ""))
    game_results = game_split[1].split(";")

    for game_result in game_results:
        cleaned_result = game_result.strip()
        color_counts = cleaned_result.split(",")
        for color_count in color_counts:
            [count, name] = color_count.strip().split(" ")

            if name in colors and int(count) > int(colors[name]):
                return 0

    return game_id
        

def calculate_game_id_sum(
        input_data: list[str], 
        color_maxima_map: ColorMaximaMap
    ) -> int:
    total_id_sum = 0

    for game in input_data:
        total_id_sum = total_id_sum + calculate_single_game_sum(game, color_maxima_map)

    return total_id_sum


if __name__ == '__main__':
    file_name = sys.argv[1]
    red_count = sys.argv[2]
    green_count = sys.argv[3]
    blue_count = sys.argv[4]

    color_maxima_map: ColorMaximaMap = {
        "red": red_count,
        "green": green_count,
        "blue": blue_count
    }

    input_data = []

    with open(file_name) as input_file:
        input_data = input_file.read().splitlines()

    game_id_sum = calculate_game_id_sum(input_data, color_maxima_map)

    print(game_id_sum)
