from utils import read_file_lines, extract_numbers_from_comma_separated

NORMAL_TIMER_RESET = 6
INITIAL_TIMER = 8
DAYS_TO_SIMULATE = 80

def get_input():
    input_lines = read_file_lines("input.txt")
    line = input_lines[0]
    lantern_fish = extract_numbers_from_comma_separated(line)
    population = [Lanternfish(timer) for timer in lantern_fish]
    return LanternfishPopulation(population)


def solve_a():
    population = get_input()
    population.x_days_pass(DAYS_TO_SIMULATE)
    return population.get_size()


class Lanternfish:
    def __init__(self, timer):
        self.timer = timer

    def __repr__(self):
        return str(self.timer)

    def reset_timer(self):
        self.timer = NORMAL_TIMER_RESET

    def day_passes(self):
        if self.timer == 0:
            self.reset_timer()
            return Lanternfish(INITIAL_TIMER)
        else:
            self.timer -= 1


class LanternfishPopulation:
    def __init__(self, lanternfish):
        self.population = lanternfish

    def day_passes(self):
        fish_to_add = []
        for fish in self.population:
            new_fish = fish.day_passes()
            if new_fish:
                fish_to_add.append(new_fish)
        self.population = self.population + fish_to_add

    def get_size(self):
        return len(self.population)

    def x_days_pass(self, x):
        for i in range(x):
            self.day_passes()


if __name__ == '__main__':
    print(solve_a())
