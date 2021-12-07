from dive.position import Position
from utils import read_file_lines


def get_input():
    lines = read_file_lines("dive/dive_input.txt")
    return lines


def make_moves(moves):
    position = Position()
    for move in moves:
        direction, amount = move.split()
        amount = int(amount)
        position.move(direction, amount)
    return position


def solve():
    moves = get_input()
    final_position = make_moves(moves)
    return final_position.multiply_position()

