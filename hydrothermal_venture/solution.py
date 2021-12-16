from utils import read_file_lines, extract_numbers_from_comma_separated


def get_input():
    input_lines = read_file_lines("input.txt")
    lines = []
    for input_line in input_lines:
        a, b = input_line.split('->')
        a_coordinates = extract_numbers_from_comma_separated(a)
        b_coordinates = extract_numbers_from_comma_separated(b)
        point_a = Point(a_coordinates[0], a_coordinates[1])
        point_b = Point(b_coordinates[0], b_coordinates[1])
        line = Line(point_a, point_b)
        lines.append(line)
    return lines


def get_intersections_from_lines(lines):
    intersections = {}
    for line in lines:
        points_on_line = line.get_points_on_line()
        for point_on_line in points_on_line:
            x, y = point_on_line.get_point()
            if intersections.get(x):
                if intersections[x].get(y):
                    intersections[x][y] += 1
                else:
                    intersections[x][y] = 1
            else:
                intersections[x] = {y: 1}

    return intersections


def count_intersections_with_two_or_more(intersections):
    count = 0
    for x, y_points in intersections.items():
        for y, intersections in y_points.items():
            if intersections >= 2:
                count += 1
    return count


def get_values_in_range(a, b):
    if a<=b:
        return [i for i in range(a, b+1)]
    else:
        return [i for i in range(a, b-1, -1)]


def solve_a():
    lines = get_input()
    intersections = get_intersections_from_lines(lines)
    return count_intersections_with_two_or_more(intersections)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def get_point(self):
        return self.x, self.y


class Line:
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def __repr__(self):
        return f"{self.point_a} -> {self.point_b}"

    def is_horizontal(self):
        return self.point_a.y == self.point_b.y

    def is_vertical(self):
        return self.point_a.x == self.point_b.x

    def get_points_on_line(self):
        if self.is_horizontal():
            x_coordinates = get_values_in_range(self.point_a.x, self.point_b.x)
            y_coordinates = [self.point_a.y for _ in x_coordinates]
        elif self.is_vertical():
            y_coordinates = get_values_in_range(self.point_a.y, self.point_b.y)
            x_coordinates = [self.point_a.x for _ in y_coordinates]
        else:
            x_coordinates = get_values_in_range(self.point_a.x, self.point_b.x)
            y_coordinates = get_values_in_range(self.point_a.y, self.point_b.y)

        # for x, y in zip(x_coordinates, y_coordinates):
        #     points.append(Point(x, y))
        points = [Point(x, y) for x, y in zip(x_coordinates, y_coordinates)]
        return points


if __name__ == '__main__':
    print(solve_a())
