import math
import re


class SnailfishNumber:
    OPEN_BRACKET = "["
    CLOSE_BRACKET = "]"
    PAIR_SEPERATOR = ","
    EXPLODE_THRESHOLD = 5
    SPLIT_THRESHOLD = 10

    def __init__(self, number):
        self.number = number

    def remove_brackets(self, text):
        return text.replace(self.OPEN_BRACKET, "").replace(self.CLOSE_BRACKET, "")

    def extract_numbers(self, text):
        text = self.remove_brackets(text)
        numbers = text.split(self.PAIR_SEPERATOR)
        return [int(number) for number in numbers if number]

    def get_outermost_pair(self, text):
        # comma after open - closed = 1
        current_level = 0
        for i in range(len(text)):
            if text[i] == self.OPEN_BRACKET:
                current_level += 1
            elif text[i] == self.CLOSE_BRACKET:
                current_level -= 1
            elif text[i] == self.PAIR_SEPERATOR and current_level == 1:
                return text[1:i], text[i + 1:-1]

    def reduce(self):
        while True:
            while self.explode():
                pass
            if not self.split():
                return

    def needs_to_split(self):
        numbers = self.extract_numbers(self.number)
        for number in numbers:
            if number >= self.SPLIT_THRESHOLD:
                return number

    def split(self):
        number_to_split = self.needs_to_split()
        if number_to_split is None:
            return False
        round_down = math.floor(number_to_split / 2)
        round_up = math.ceil(number_to_split / 2)
        start_index = self.number.find(str(number_to_split))
        length = (len(str(number_to_split)))
        end_index = start_index + length
        self.number = f"{self.number[:start_index]}[{round_down},{round_up}]{self.number[end_index:]}"
        return True

    def needs_to_explode(self):
        current_level = 0
        for i in range(len(self.number)):
            if self.number[i] == self.OPEN_BRACKET:
                current_level += 1
            elif self.number[i] == self.CLOSE_BRACKET:
                current_level -= 1
            if current_level == self.EXPLODE_THRESHOLD:
                return i

    def explode(self):
        start_index = self.needs_to_explode()
        if start_index is None:
            return False

        end_index = start_index + self.number[start_index:].find(self.CLOSE_BRACKET)
        left_value, right_value = self.extract_numbers(self.number[start_index:end_index + 1])
        left_string = self.number[0:start_index]
        right_string = self.number[end_index + 1:]
        updated_left = self.add_left_explosion_to_next_left(left_string, left_value)
        updated_right = self.add_right_explosion_to_next_right(right_string, right_value)
        self.number = f"{updated_left}0{updated_right}"
        return True

    def add_left_explosion_to_next_left(self, left_string, left_explosion_value):
        numbers = self.extract_numbers(left_string)
        if len(numbers) < 1:
            return left_string
        next_left_value = numbers[-1]
        length = len(str(next_left_value))
        start_index_of_left = left_string.rfind(str(next_left_value))
        end_index_of_left = start_index_of_left + length

        return f"{left_string[0:start_index_of_left]}{next_left_value+left_explosion_value}{left_string[end_index_of_left:]}"

    def add_right_explosion_to_next_right(self, right_string, right_explosion_value):
        numbers = self.extract_numbers(right_string)
        if len(numbers) < 1:
            return right_string
        next_right_value = numbers[0]
        length = len(str(next_right_value))
        start_index_of_right = right_string.find(str(next_right_value))
        end_index_of_right = start_index_of_right + length

        return f"{right_string[0:start_index_of_right]}{next_right_value + right_explosion_value}{right_string[end_index_of_right:]}"

    @staticmethod
    def is_simple_pair(text):
        return bool(re.match(r"\[\d+,\d+\]", text))

    def calculate_magnitude(self):
        return self.calculate_magnitude_helper(self.number)

    def calculate_magnitude_helper(self, number):
        left, right = self.get_outermost_pair(number)
        if left.isdigit() and right.isdigit():
            return 3 * int(left) + 2*int(right)
        elif left.isdigit():
            return 3 * int(left) + 2 * self.calculate_magnitude_helper(right)
        elif right.isdigit():
            return 3 * self.calculate_magnitude_helper(left) + 2 * int(right)
        else:
            return 3 * self.calculate_magnitude_helper(left) + 2 * self.calculate_magnitude_helper(right)

    def add(self, snailfish_number):
        self.number = f"[{self.number},{snailfish_number.number}]"
        self.reduce()
