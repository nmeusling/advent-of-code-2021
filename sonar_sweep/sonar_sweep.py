from utils import read_file_lines, extract_numbers


def get_input():
    file_path = "sonar_sweep/sonar_sweep_input.txt"
    lines = read_file_lines(file_path)
    numbers = extract_numbers(lines)
    return numbers


def count_increases(numbers):
    number_of_increases = 0
    for i, number in enumerate(numbers):
        if i > 0 and number > numbers[i-1]:
            number_of_increases += 1
    return number_of_increases


def create_sums(numbers):
    sums = []
    number_of_sums = len(numbers) - 2
    if number_of_sums < 1:
        return 0
    for i in range(number_of_sums):
        sums.append(numbers[i] + numbers[i+1] + numbers[i+2])
    return sums


def solve_a():
    numbers = get_input()
    return count_increases(numbers)


def solve_b():
    numbers = get_input()
    sums = create_sums(numbers)
    return count_increases(sums)
