def read_file_lines(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    return lines


def remove_white_space(lines):
    formatted_lines = []
    for line in lines:
        formatted_lines.append(line.strip())
    return formatted_lines


def extract_numbers(numbers):
    extracted_numbers = []
    for number in numbers:
        number = number.strip()
        extracted_numbers.append(int(number))
    return extracted_numbers
