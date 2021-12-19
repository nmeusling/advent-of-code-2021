import re

from beacon_scanner.point import Point
from utils import read_file_lines, remove_white_space, extract_numbers_from_comma_separated


def get_input():
    lines = read_file_lines("input.txt")
    lines = remove_white_space(lines)
    scanners = {}
    current_scanner = -1
    for line in lines:
        scanner = is_scanner_header(line)
        if scanner != -1:
            current_scanner = scanner
        if scanner == -1:
            if line:
                # only care if line is not blank
                beacons = extract_numbers_from_comma_separated(line)
                if current_scanner in scanners:
                    scanners[current_scanner].append(beacons)
                else:
                    scanners[current_scanner] = [beacons]
    return scanners


def is_scanner_header(line):
    pattern = r"--- scanner \d+ ---"
    if re.match(pattern, line):
        match = re.findall("\d+", line)
        return int(match[0])
    return -1

def get_distances_between_beacons_for_scanner(beacons):
    # can only do half triangle because itś commutative
    distances = [ [0]*len(beacons) for i in range(len(beacons))]
    for i, beacon in enumerate(beacons):
        for j, second_beacon in enumerate(beacons):
            first_beacon = Point(beacon[0], beacon[1], beacon[2])
            second_beacon = Point(second_beacon[0], second_beacon[1], second_beacon[2])
            distance = first_beacon.calculate_distance(second_beacon)
            distances[i][j] = distance
    return distances

def get_all_distances(distances_between_beacons):
    distances = set()
    for row in distances_between_beacons:
        for column in row:
            distances.add(column)
    return distances

def solve_a():
    scanners = get_input()
    distances = get_distances_between_beacons_for_scanner(scanners[0])
    for line in distances:
        print(line)
    a_distances = get_all_distances(distances)
    print(a_distances)

    distances_two = get_distances_between_beacons_for_scanner(scanners[1])
    for line in distances_two:
        print(line)
    b_distances = get_all_distances(distances_two)
    print(b_distances)

    print("\n\n\n\n")
    common_distances = a_distances.intersection(b_distances)
    print(common_distances)
    print(len(common_distances))

    beacons = set()
    for i, row in enumerate(distances):
        for j, value in enumerate(row):
            if value in common_distances:
                beacons.add(i)
                beacons.add(j)
    print("\n\n\n\n")
    print(beacons)
    print(len(beacons))



    return None


def solve_b():
    pass

if __name__ == '__main__':
    print(solve_a())
