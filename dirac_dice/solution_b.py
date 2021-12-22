from collections import defaultdict
from itertools import product

from utils import read_file_lines


def get_input():
    lines = read_file_lines("input.txt")
    lines = [line.split()[-1] for line in lines]
    return int(lines[0]), int(lines[1])


def get_roll_possibilities():
    dice_values = [1, 2, 3]
    combinations = [sum(combination) for combination in product(dice_values, repeat=3)]
    combination_counts = defaultdict(int)
    for combination in combinations:
        combination_counts[combination] += 1
    return combination_counts


def make_move(position, score, places_to_move):
    new_position = (position + places_to_move - 1) % 10 + 1
    return new_position, score + new_position


def get_possible_states(position, length_dict, score=0, turns=0, weight=1):
    for roll_sum, count in get_roll_possibilities().items():
        if score >= 21:
            return
        new_position, new_score = make_move(position, score, roll_sum)
        new_turns = turns + 1
        new_weight = weight*count
        length_dict[(new_turns, new_score)] += new_weight
        get_possible_states(new_position, length_dict, new_score, new_turns, new_weight)


def get_possible_states_both_players(player_starts):
    possible_states_both_players = []
    for i, player in enumerate(player_starts):
        possible_states = defaultdict(int)
        get_possible_states(player_starts[i], possible_states)
        possible_states_both_players.append(possible_states)
    return possible_states_both_players


def count_wins(possible_states):
    wins = [0, 0]
    for (p1_turns, p1_score), p1_count in possible_states[0].items():
        for (p2_turns, p2_score), p2_count in possible_states[1].items():
            # p1 wins, score is over 21, has one more move than p2 and p2 is under 21
            if p1_score >= 21 and p1_turns == p2_turns + 1 and p2_score < 21:
                wins[0] += p1_count * p2_count
            # p2 wins
            elif p2_score >= 21 and p2_turns == p1_turns and p1_score < 21:
                wins[1] += p1_count * p2_count
    return wins


def solve_b():
    player_starts = get_input()
    possible_states = get_possible_states_both_players(player_starts)
    return count_wins(possible_states)


if __name__ == '__main__':
    print(max(solve_b()))
