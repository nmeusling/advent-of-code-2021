from snailfish.snail_number import SnailfishNumber
from utils import read_file_lines, remove_white_space


def get_input():
    input_lines = read_file_lines("input.txt")
    lines = remove_white_space(input_lines)
    numbers = [SnailfishNumber(line) for line in lines]
    return numbers


def solve_a():
    numbers = get_input()
    sum = numbers[0]
    for i in range(1,len(numbers)):
        sum.add(numbers[i])
    return sum.calculate_magnitude()


def solve_b():
    max_magnitude = 0
    numbers = get_input()
    for first_number in numbers:
        for second_number in numbers:
            if first_number != second_number:
                sum = SnailfishNumber(first_number.number)
                sum.add(second_number)
                magnitude = sum.calculate_magnitude()
                if magnitude > max_magnitude:
                    max_magnitude = magnitude
    return max_magnitude


if __name__ == '__main__':
    print(solve_a())
    print(solve_b())
