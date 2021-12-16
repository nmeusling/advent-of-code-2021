from utils import read_file_lines, extract_numbers_from_comma_separated

NORMAL_TIMER_RESET = 6
INITIAL_TIMER = 8
DAYS_TO_SIMULATE = 256


def get_input():
    input_lines = read_file_lines("input.txt")
    lantern_fish = extract_numbers_from_comma_separated(input_lines[0])
    population = LanternfishPopulation()
    population.add_multiple_fish(lantern_fish)
    return population


def solve_b():
    population = get_input()
    population.x_days_pass(DAYS_TO_SIMULATE)
    return population.get_size()


class LanternfishPopulation:
    def __init__(self):
        self.population = {}
        self.initialize_population()

    def initialize_population(self):
        for i in range(INITIAL_TIMER + 1):
            self.population[i] = 0

    def add_multiple_fish(self, all_fish):
        for fish in all_fish:
            self.add_fish(fish)

    def add_fish(self, timer):
        self.population[timer] += 1

    def day_passes(self):
        ready_to_reproduce = self.population[0]
        for i in range(1, INITIAL_TIMER+1):
            self.population[i-1] = self.population[i]
        self.population[NORMAL_TIMER_RESET] += ready_to_reproduce
        self.population[INITIAL_TIMER] = ready_to_reproduce

    def x_days_pass(self, x):
        for i in range(x):
            self.day_passes()

    def get_size(self):
        population_size = 0
        for timer, count in self.population.items():
            population_size += count
        return population_size


if __name__ == '__main__':
    print(solve_b())