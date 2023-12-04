import sys

def calculate_points(card: str) -> int:
    points = 0
    name_split = card.split(":")
    game_split = name_split[1].split("|")

    # https://www.reddit.com/r/adventofcode/comments/18aexku/2023_day_4python_did_you_know_stringsplit_is_not/
    # Turns out I made the mistake of splitting wrong.
    winning_numbers = set(game_split[0].strip().split())
    my_numbers = game_split[1].strip().split()

    for number in my_numbers:
        if number in winning_numbers:
            if points == 0:
                points = 1
            else:
                points *= 2

    return points

def calculate_wins(card: str):
    wins = 0
    name_split = card.split(":")
    game_split = name_split[1].split("|")

    winning_numbers = set(game_split[0].strip().split())
    my_numbers = game_split[1].strip().split()

    for number in my_numbers:
        if number in winning_numbers:
            wins += 1

    return wins

def part_1(input: list[str]):
    point_count = 0
    for card in input:
        point_count += calculate_points(card)
    
    print(point_count)
        
def part_2(input: list[str]):
    card_counts = {}

    for i in range(len(input)):
        card_counts[str(i + 1)] = 1

    for i in range(len(input)):
        win_count = calculate_wins(input[i])
        for j in range(win_count):
            card_counts[str(i + 1 + j + 1)] += 1 * card_counts[str(i + 1)]


    # calculate # of wins.
    # Use that to increase counts.
    # Sum all counts at end.
    print(sum([card_counts[key] for key in card_counts]))


if __name__ == '__main__':
    file_name = sys.argv[1]
    file_data: list[str] = []

    with open(file_name) as input_file:
        file_data = input_file.read().splitlines()

    part_1(file_data)
    part_2(file_data)