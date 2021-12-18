from itertools import product

from utils import read_file_lines


class Target:
    def __init__(self, x_range, y_range):
        self.x_min = min(x_range)
        self.x_max = max(x_range)
        self.y_min = min(y_range)
        self.y_max = max(y_range)

    def x_is_in_target(self, x):
        return self.x_min <= x <= self.x_max

    def y_is_in_target(self, y):
        return self.y_min <= y <= self.y_max


def get_target():
    input_lines = read_file_lines("input.txt")
    extracted = input_lines[0].replace("target area: x=", "").replace(" y=", "")
    x, y = extracted.split(",")
    x_range = x.split("..")
    x_range = [int(x) for x in x_range]
    y_range = y.split("..")
    y_range = [int(y) for y in y_range]
    return Target(x_range, y_range)


def get_y_velocity_for_max_height(y_min):
    # Max height is the highest y velocity without overshooting the y-min
    return -(y_min + 1)


def get_max_height(y_velocity):
    return sum(range(y_velocity, 0, -1))


def probe_will_reach_target_in_n_steps_at_x_velocity(steps, x_velocity, target):
    x = 0
    for i in range(steps):
        x += x_velocity
        if x_velocity > 0:
            x_velocity -= 1
        elif x_velocity == 0:
            return target.x_is_in_target(x)
    return target.x_is_in_target(x)


def get_velocities_for_x_to_reach_target_in_n_steps(steps, target):
    results = []
    for velocity_x in range(1, target.x_max + 1):
        if probe_will_reach_target_in_n_steps_at_x_velocity(steps, velocity_x, target):
            results.append(velocity_x)
    return results


def get_x_velocities_for_valid_y_steps(valid_y_steps, target):
    x_velocities_by_step = {}
    for steps, y_velocities in valid_y_steps.items():
        velocities = get_velocities_for_x_to_reach_target_in_n_steps(steps, target)
        if velocities:
            x_velocities_by_step[steps] = velocities
    return x_velocities_by_step


def get_number_of_steps_for_velocity_y_to_reach_target(y_velocity, target):
    y = 0
    steps = 0
    valid_steps = []
    while y >= target.y_min:
        steps += 1
        y += y_velocity

        y_velocity -= 1
        if target.y_is_in_target(y):
            valid_steps.append(steps)
    return valid_steps


def get_number_of_steps_per_initial_y_velocities(target):
    steps_per_velocity = {}
    min_velocity = target.y_min
    max_velocity = get_y_velocity_for_max_height(target.y_min)
    for velocity in range(min_velocity, max_velocity + 1):
        valid_steps = get_number_of_steps_for_velocity_y_to_reach_target(velocity, target)
        if valid_steps:
            steps_per_velocity[velocity] = valid_steps
    return steps_per_velocity


def get_velocity_per_steps(steps_per_velocity):
    # Convert steps per velocity dict into velocity per steps for easier comparison
    velocity_per_steps = {}
    for velocity, steps in steps_per_velocity.items():
        for step in steps:
            if step in velocity_per_steps:
                velocity_per_steps[step].append(velocity)
            else:
                velocity_per_steps[step] = [velocity]
    return velocity_per_steps


def count_possibilities(x_velocities_per_step, y_velocities_per_step):
    possibilities = set()
    for step, x_velocities in x_velocities_per_step.items():
        if step in y_velocities_per_step:
            combinations = set(product(x_velocities, y_velocities_per_step[step]))
            possibilities = possibilities.union(combinations)
    return len(possibilities)


def solve_a():
    target = get_target()
    y_vel = get_y_velocity_for_max_height(target.y_min)
    return get_max_height(y_vel)


def solve_b():
    target = get_target()
    y_steps = get_number_of_steps_per_initial_y_velocities(target)
    y_velocity_per_steps = get_velocity_per_steps(y_steps)
    x_velocities_per_steps = get_x_velocities_for_valid_y_steps(y_velocity_per_steps, target)
    num_possibilities = count_possibilities(x_velocities_per_steps, y_velocity_per_steps)
    return num_possibilities


if __name__ == '__main__':
    print(solve_a())
    print(solve_b())
