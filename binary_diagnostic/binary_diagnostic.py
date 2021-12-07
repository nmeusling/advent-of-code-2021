from utils import read_file_lines, remove_white_space


def get_input():
    lines = read_file_lines("binary_diagnostic./binary_diagnostic_input.txt")
    lines = remove_white_space(lines)
    return lines


def get_gamma_and_epsilon(diagnostic_numbers):
    length_of_line = len(diagnostic_numbers[0])
    gamma_rate = ""
    epsilon_rate = ""
    for position in range(length_of_line):
        values = [int(line[position]) for line in diagnostic_numbers]
        average = sum(values)/len(diagnostic_numbers)
        if average >= .5:
            gamma_rate = gamma_rate + "1"
            epsilon_rate = epsilon_rate + "0"
        else:
            gamma_rate = gamma_rate + "0"
            epsilon_rate = epsilon_rate + "1"
    return gamma_rate, epsilon_rate


def get_oxygen_rating(diagnostic_numbers):
    length_of_line = len(diagnostic_numbers[0])
    oxygen_generator = ""
    for position in range(length_of_line):
        values = [int(line[position]) for line in diagnostic_numbers]
        average = sum(values) / len(diagnostic_numbers)
        if average >= .5:
            oxygen_generator = oxygen_generator + "1"
        else:
            oxygen_generator = oxygen_generator + "0"
        diagnostic_numbers = filter_numbers(diagnostic_numbers, oxygen_generator)
    return oxygen_generator


def get_co2_rating(diagnostic_numbers):
    length_of_line = len(diagnostic_numbers[0])
    co2_scrubber = ""
    for position in range(length_of_line):
        values = [int(line[position]) for line in diagnostic_numbers]
        average = sum(values) / len(diagnostic_numbers)
        if average >= .5:
            co2_scrubber = co2_scrubber + "0"
        else:
            co2_scrubber = co2_scrubber + "1"
        diagnostic_numbers = filter_numbers(diagnostic_numbers, co2_scrubber)
        if len(diagnostic_numbers) <= 1:
            return diagnostic_numbers[0]
    return co2_scrubber


def filter_numbers(diagnostic_numbers, criteria):
    filtered_numbers = []
    for number in diagnostic_numbers:
        if number.startswith(criteria):
            filtered_numbers.append(number)
    return filtered_numbers


def solve():
    lines = get_input()
    gamma, epsilon = get_gamma_and_epsilon(lines)
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma*epsilon


def solve_b():
    lines = get_input()
    oxygen = get_oxygen_rating(lines)
    co2 = get_co2_rating(lines)
    oxygen = int(oxygen, 2)
    co2 = int(co2, 2)
    return oxygen * co2
