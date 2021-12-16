from copy import copy, deepcopy

from utils import read_file_lines, extract_numbers_from_comma_separated

BOARD_DIMENSION = 5
NUM_LINES_BETWEEN_BOARDS = 1


def get_input():
    lines = read_file_lines("input.txt")
    chosen_numbers = extract_numbers_from_comma_separated(lines[0])
    boards = get_list_of_boards(lines)
    return chosen_numbers, boards


def get_list_of_boards(board_lines):
    boards = []
    start_index = 2
    while start_index < len(board_lines):
        boards.append(get_board(board_lines[start_index:start_index+BOARD_DIMENSION]))
        start_index = start_index + BOARD_DIMENSION + NUM_LINES_BETWEEN_BOARDS
    return boards


def get_board(board_lines):
    board = []
    for row in board_lines:
        values = row.split()
        values = [int(value) for value in values]
        board.append(values)
    return board


def make_moves_and_find_score(boards, numbers):
    for number in numbers:
        for board in boards:
            if board.mark_square(number):
                return board.sum_unmarked() * number


def find_score_last_winning_board(boards, numbers):
    num_of_wins = 0
    total_boards = len(boards)
    ongoing_boards = []
    for number in numbers:
        board_indices_that_won = []
        for i, board in enumerate(boards):
            if board.mark_square(number):
                board_indices_that_won.append(i)
                num_of_wins += 1
                if num_of_wins >= total_boards:
                    return board.sum_unmarked() * number
        for index in reversed(board_indices_that_won):
            boards.pop(index)



def solve_a():
    chosen_numbers, input_boards = get_input()
    boards = []
    for board in input_boards:
        boards.append(Board(board))
    return make_moves_and_find_score(boards, chosen_numbers)


def solve_b():
    chosen_numbers, input_boards = get_input()
    boards = []
    for board in input_boards:
        boards.append(Board(board))
    return find_score_last_winning_board(boards, chosen_numbers)


class Board:
    def __init__(self, board):
        self.board = []
        self.has_won = False
        for i in range(BOARD_DIMENSION):
            self.board.append([])
            for j in range(BOARD_DIMENSION):
                square = Square(board[i][j])
                self.board[i].append(square)

    def find_value_on_board(self, value):
        for i, row in enumerate(self.board):
            for j, square in enumerate(row):
                if square.value == value:
                    return i, j
        return None

    def mark_square(self, value):
        value_found = self.find_value_on_board(value)
        if not value_found:
            return False
        row, column = value_found
        self.board[row][column].is_marked = True
        if self.check_board_win(row, column):
            self.has_won = True
            return True
        return False

    def column_has_win(self, column):
        column_win = True
        for i in range(BOARD_DIMENSION):
            square = self.board[i][column]
            if not square.is_marked:
                column_win = False
        return column_win

    def row_has_win(self, row):
        row_win = True
        for square in self.board[row]:
            if not square.is_marked:
                row_win = False
        if row_win:
            return row_win

    def check_board_win(self, row, column):
        return self.column_has_win(column) or self.row_has_win(row)

    def sum_unmarked(self):
        sum = 0
        for row in self.board:
            for square in row:
                if not square.is_marked:
                    sum += square.value
        return sum


class Square:
    def __init__(self, value):
        self.value = value
        self.is_marked = False

    def __repr__(self):
        return f"val/marked {self.value}/{self.is_marked}"

#
# class BoardList:
#     def __init__(self, boards):
#         self.boards = boards
#         self.won_boards = []
#
#     def make_move(self, number):
#         for i, board in enumerate(self.boards):
#             if board.mark_square(number):
#                 self.won_boards.append(board)
#



if __name__ == '__main__':
    # print(solve_a())
    print(solve_b())

    # chosen_numbers, input_boards = get_input()
    # boards = []
    # for board in input_boards:
    #     boards.append(Board(board))
    # numbers = [15, 61, 58, 80, 71]
    # find_score_last_winning_board(boards, numbers)

