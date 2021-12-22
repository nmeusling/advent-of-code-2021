from utils import read_file_lines


class Player:
    def __init__(self, position):
        self.position = position
        self.score = 0

    def make_move(self, sum_of_dice):
        new_position = (sum_of_dice + self.position) % 10
        if new_position == 0:
            new_position = 10
        self.position = new_position
        self.score += new_position
        if self.score >= 1000:
            return True
        return False


class Dice:
    def __init__(self):
        self.roll_number = 0

    def roll_dice(self):
        sum_next_three = self.roll_number*9 + 6
        self.roll_number += 1
        return sum_next_three


class Game:
    def __init__(self, player_one, player_two):
        self.players = {
            1: player_one,
            2: player_two
        }
        self.active_player = 1
        self.inactive_player = 2
        self.turns = 0
        self.dice = Dice()

    def toggle_active_player(self):
        if self.active_player == 1:
            self.active_player = 2
            self.inactive_player = 1
        else:
            self.active_player = 1
            self.inactive_player = 2

    def make_move(self, sum_of_dice):
        has_won = self.players[self.active_player].make_move(sum_of_dice)
        self.turns += 1
        if has_won:
            return True
        else:
            self.toggle_active_player()

    def play_game(self):
        has_won = False
        while not has_won:
            dice = self.dice.roll_dice()
            has_won = self.make_move(dice)
        loser_score = self.players[self.inactive_player].score
        dice_rolls = self.turns*3
        return loser_score * dice_rolls


def get_input():
    lines = read_file_lines("input.txt")
    lines = [line.split()[-1] for line in lines]
    return int(lines[0]), int(lines[1])


def solve_a():
    player_one_start, player_two_start = get_input()
    player_one = Player(player_one_start)
    player_two = Player(player_two_start)
    game = Game(player_one, player_two)
    return game.play_game()


if __name__ == '__main__':
    print(solve_a())
