import math
import re

from utils import read_file_lines, remove_white_space

OPEN_BRACKET = "["
CLOSE_BRACKET = "]"
PAIR_SEPERATOR = ","
EXPLODE_THRESHOLD = 5
SPLIT_THRESHOLD = 10


def get_input():
    input_lines = read_file_lines("input.txt")
    lines = remove_white_space(input_lines)
    return lines


def split_outer_pair(starfish_number):
    # comma after open - closed = 1
    current_level = 0
    for i in range(len(starfish_number)):
        if starfish_number[i] == OPEN_BRACKET:
            current_level += 1
        elif starfish_number[i] == CLOSE_BRACKET:
            current_level -= 1
        elif starfish_number[i] == PAIR_SEPERATOR and current_level == 1:
            return starfish_number[1:i], starfish_number[i+1:-1]


def needs_to_reduce(starfish_number):
    return needs_to_split(starfish_number) or needs_to_explode(starfish_number)


#TODO split method should use this, return int
def needs_to_split(starfish_number):
    numbers = extract_all_numbers(starfish_number)
    for number in numbers:
        if number >= SPLIT_THRESHOLD:
            return True
    return False


#TODO split method should use this, return int
def needs_to_explode(starfish_number):
    current_level = 0
    for i in range(len(starfish_number)):
        if starfish_number[i] == OPEN_BRACKET:
            current_level += 1
        elif starfish_number[i] == CLOSE_BRACKET:
            current_level -= 1
        if current_level == 5:
            return True
    return False

def split(starfish_number):
    numbers = extract_all_numbers(starfish_number)
    for number in numbers:
        if number >= SPLIT_THRESHOLD:
            round_down = math.floor(number/2)
            round_up = math.ceil(number/2)
            start_index = starfish_number.find(str(number))
            length = (len(str(number)))
            end_index = start_index + length
            return f"{starfish_number[:start_index]}[{round_down},{round_up}]{starfish_number[end_index:]}"
    return starfish_number


def explode(starfish_number):
    current_level = 0
    for i in range(len(starfish_number)):
        if starfish_number[i] == OPEN_BRACKET:
            current_level += 1
        elif starfish_number[i] == CLOSE_BRACKET:
            current_level -= 1
        if current_level == EXPLODE_THRESHOLD:
            next_closing_bracket = starfish_number[i:].find(CLOSE_BRACKET)
            left_value, right_value = extract_numbers_from_pair(starfish_number[i:i+next_closing_bracket+1])
            left_string = starfish_number[0:i]
            right_string = starfish_number[i+next_closing_bracket+1:]
            updated_left = add_left_explosion_to_next_left(left_string, left_value)
            updated_right = add_right_explosion_to_next_right(right_string, right_value)
            return f"{updated_left}0{updated_right}"
    return starfish_number


def replace_pair_with_zero(start, end, starfish_number):
    updated = f"{starfish_number[0:start]}0{starfish_number[end+1:]}"
    return updated


def add_left_explosion_to_next_left(left_string, left_explosion_value):
    without_brackets = remove_brackets(left_string)
    separated = without_brackets.split(PAIR_SEPERATOR)
    if len(separated) < 2:
        return left_string
    next_left_value = without_brackets.split(PAIR_SEPERATOR)[-2]
    #TODO do we need this?
    if not next_left_value:
        # There are no numbers left of start
        return left_string
    length = len(next_left_value)
    start_index_of_left = left_string.rfind(next_left_value)
    end_index_of_left = start_index_of_left + length
    next_left_value = int(next_left_value)

    updated_left_string = f"{left_string[0:start_index_of_left]}{next_left_value+left_explosion_value}{left_string[end_index_of_left:]}"
    return updated_left_string
#TODO should we make a class for snailfish number?


def add_right_explosion_to_next_right(right_string, right_explosion_value):
    without_brackets = remove_brackets(right_string)
    # Is this 0 or 1?
    separated = without_brackets.split(PAIR_SEPERATOR)
    if len(separated) < 2:
        return right_string
    next_right_value = separated[1]
    #TODO do we still need this
    if not next_right_value:
        # There are no numbers left of start
        return right_string
    length = len(next_right_value)
    start_index_of_right = right_string.find(next_right_value)
    end_index_of_right = start_index_of_right + length
    next_right_value = int(next_right_value)

    updated_right_string = f"{right_string[0:start_index_of_right]}{next_right_value + right_explosion_value}{right_string[end_index_of_right:]}"
    return updated_right_string


def remove_brackets(text):
    return text.replace(OPEN_BRACKET, "").replace(CLOSE_BRACKET, "")


def extract_numbers_from_pair(text):
    text = remove_brackets(text)
    left, right = text.split(PAIR_SEPERATOR)
    return int(left), int(right)

def is_simple_pair(text):
    return bool(re.match("\[\d+,\d+\]", text))

def extract_all_numbers(text):
    text = remove_brackets(text)
    numbers = text.split(PAIR_SEPERATOR)
    return [int(number) for number in numbers]


def add_snailfish(first, second):
    sum = f"[{first},{second}]"
    sum = reduce(sum)
    return sum


def reduce(number):
    while needs_to_reduce(number):
        while needs_to_explode(number):
            number = explode(number)
        number = split(number)
    return number


def calculate_magnitude(snailfish_number):
    if is_simple_pair(snailfish_number):
        left, right = extract_numbers_from_pair(snailfish_number)
        return 3*left + 2*right
    left, right = split_outer_pair(snailfish_number)
    return 3 * calculate_magnitude(left) + 2 * calculate_magnitude(right)


def solve_a():
    numbers = get_input()
    sum = numbers[0]
    for i in range(1,len(numbers)):
        sum = add_snailfish(sum, numbers[i])

    return calculate_magnitude(sum)


if __name__ == '__main__':
    # test2 = "[[[[[9,8],1],2],3],4]"
    # test3 = "[[[[0,7],4],[7,[[8,4],9]]],[1,1]]"
    # test4 = "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]"
    # a = "[[[[4,3],4],4],[7,[[8,4],9]]]"
    # b = "[1,1]"
    # sum = add_snailfish(a, b)
    # print(explode(test3))
    # print(split(test4))
    # print(reduce(sum))
    # a = "[[[[4,3],4],4],[7,[[8,4],9]]]"
    # b = "[1,1]"
    # print(add_snailfish(a, b))
    print(solve_a())

