from utils import read_file_lines, extract_numbers_from_comma_separated


def get_input():
    lines = read_file_lines("input.txt")
    values = extract_numbers_from_comma_separated(lines[0])
    return values


def get_fuel_to_align_at_position_constant_fuel(crabs, position):
    fuel_used = [abs(crab - position) for crab in crabs]
    return sum(fuel_used)


def get_fuel_to_align_at_position(crabs, position):
    fuel_used = [sum(range(abs(crab-position) + 1)) for crab in crabs]
    return sum(fuel_used)


def get_minimum_fuel_to_align(positions, constant_fuel=False):
    minimum_fuel = None
    min_position = min(positions)
    max_position = max(positions)
    for position in range(min_position, max_position + 1):
        if constant_fuel:
            fuel_used = get_fuel_to_align_at_position_constant_fuel(positions, position)
        else:
            fuel_used = get_fuel_to_align_at_position(positions, position)
        if minimum_fuel is None or fuel_used < minimum_fuel:
            minimum_fuel = fuel_used
    return minimum_fuel


def solve_a():
    crabs = get_input()
    return get_minimum_fuel_to_align(crabs, constant_fuel=True)


def solve_b():
    crabs = get_input()
    return get_minimum_fuel_to_align(crabs, constant_fuel=False)


if __name__ == '__main__':
    print(solve_a())
    print(solve_b())
