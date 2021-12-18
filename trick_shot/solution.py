from itertools import product

from utils import read_file_lines


def get_input():
    input_lines = read_file_lines("input.txt")
    extracted = input_lines[0].replace("target area: x=", "").replace(" y=", "")
    x, y = extracted.split(",")
    x_min, x_max = x.split("..")
    y_min, y_max = y.split("..")
    return (int(x_min), int(x_max)), (int(y_min), int(y_max))


def get_y_velocity_for_highest(y_min):
    return -(y_min + 1)


def get_max_height(y_velocity):
    return sum(range(y_velocity, 0, -1))


def probe_will_reach_target_in_n_steps_at_x_velocity(steps, x_velocity, x_min, x_max):
    x = 0
    for i in range(steps):
        x += x_velocity
        if x_velocity > 0:
            x_velocity -= 1
        elif x_velocity == 0:
            return x_min <= x <= x_max
    return x_min <= x <= x_max


def get_velocities_for_x_to_reach_target_in_n_steps(steps, x_min, x_max):
    results = []
    for velocity_x in range(1, x_max + 1):
        if probe_will_reach_target_in_n_steps_at_x_velocity(steps, velocity_x, x_min, x_max):
            results.append(velocity_x)
    return results


def get_x_velocities_for_valid_y_steps(valid_y_steps, x_min, x_max):
    x_velocities_by_step = {}
    for steps, y_velocities in valid_y_steps.items():
        velocities = get_velocities_for_x_to_reach_target_in_n_steps(steps, x_min, x_max)
        if velocities:
            x_velocities_by_step[steps] = velocities
    return x_velocities_by_step


def get_number_of_steps_for_velocity_y_to_reach_target(y_velocity, y_min, y_max):
    y = 0
    steps = 0
    valid_steps = []
    while y >= y_min:
        steps += 1
        y += y_velocity

        y_velocity -= 1
        if y_min <= y <= y_max:
            valid_steps.append(steps)
    return valid_steps


def get_number_of_steps_per_initial_y_velocities(y_min, y_max):
    steps_per_velocity = {}
    min_velocity = y_min
    max_velocity = get_y_velocity_for_highest(y_min)
    for velocity in range(min_velocity, max_velocity + 1):
        valid_steps = get_number_of_steps_for_velocity_y_to_reach_target(velocity, y_min, y_max)
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
    x, y = get_input()
    y_vel = get_y_velocity_for_highest(y[0])
    return get_max_height(y_vel)


def solve_b():
    x, y = get_input()
    y_steps = get_number_of_steps_per_initial_y_velocities(y[0], y[1])
    y_velocity_per_steps = get_velocity_per_steps(y_steps)
    x_velocities_per_steps = get_x_velocities_for_valid_y_steps(y_velocity_per_steps, x[0], x[1])
    num_possibilities = count_possibilities(x_velocities_per_steps, y_velocity_per_steps)
    return num_possibilities


if __name__ == '__main__':
    print(solve_a())
    print(solve_b())
