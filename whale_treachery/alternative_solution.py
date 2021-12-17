from utils import read_file_lines, extract_numbers_from_comma_separated


def get_input():
    lines = read_file_lines("input.txt")
    values = extract_numbers_from_comma_separated(lines[0])
    return values


def get_fuel_to_align_at_position(crabs, position, constant_fuel):
    movement_counts = {}
    for crab in crabs:
        spaces_to_move = abs(crab - position)
        if spaces_to_move not in movement_counts:
            movement_counts[spaces_to_move] = 1
        else:
            movement_counts[spaces_to_move] += 1
    fuel_used = 0
    for spaces_to_move, count in movement_counts.items():
        fuel_used += count * calculate_fuel_cost_for_movement(spaces_to_move, constant_fuel)
    return fuel_used


def calculate_fuel_cost_for_movement(spaces_to_move, constant_fuel):
    if constant_fuel:
        return spaces_to_move
    else:
        return sum(range(spaces_to_move + 1))


def get_minimum_fuel_to_align(positions, constant_fuel=False):
    minimum_fuel = None
    min_position = min(positions)
    max_position = max(positions)
    for position in range(min_position, max_position + 1):
        fuel_used = get_fuel_to_align_at_position(positions, position, constant_fuel)
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
    # print(solve_a())
    print(solve_b())