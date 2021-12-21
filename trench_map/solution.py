from copy import copy

from utils import read_file_lines


def get_input():
    lines = read_file_lines("input.txt")
    enhancement_algorithm = convert_to_0_and_1s(lines[0]).strip()
    input_image = [convert_to_0_and_1s(line).strip() for line in lines[2:]]
    return enhancement_algorithm, input_image


def convert_to_0_and_1s(text):
    return text.replace("#", "1").replace(".", "0")


def add_border(input_image, border_size, character_for_border="0"):
    for i, line in enumerate(input_image):
        input_image[i] = f"{character_for_border*border_size}{line}{character_for_border*border_size}"
    length = len(input_image[0])
    for i in range(border_size):
        input_image.insert(0, character_for_border*length)
    for i in range(border_size):
        input_image.append(character_for_border*length)
    return input_image


def trim_border(image, size_to_trim):
    for i in range(size_to_trim):
        image.pop(-1)
    for i in range(size_to_trim):
        image.pop(0)
    for i, line in enumerate(image):
        image[i] = f"{line[size_to_trim:-size_to_trim]}"
    return image


def process_image(input_image, enhancement_algorithm):
    new_image = copy(input_image)
    for i in range(1, len(input_image)-1):
        image_line_start = input_image[i][0]
        image_line = ""
        image_line_end = input_image[i][-1]
        for j in range(1, len(input_image[i])-1):
            binary_code = f"{input_image[i-1][j-1:j+2]}{input_image[i][j-1:j+2]}{input_image[i+1][j-1:j+2]}"
            enhanced_pixel = enhancement_algorithm[get_decimal_version_of_binary_code(binary_code)]
            image_line = f"{image_line}{enhanced_pixel}"
        new_image[i] = f"{image_line_start}{image_line}{image_line_end}"
    return new_image


def count_lit_pixels(image):
    count = 0
    for line in image:
        for pixel in line:
            if pixel == "1":
                count += 1
    return count


def get_decimal_version_of_binary_code(binary_code):
    return int(binary_code, 2)


def solve_a():
    enhancement_algorithm, input_image = get_input()
    add_border(input_image, 110, "0")
    for i in range(50):
        input_image = process_image(input_image, enhancement_algorithm)
    trim_border(input_image, 60)
    return count_lit_pixels(input_image)


if __name__ == '__main__':
    print(solve_a())
