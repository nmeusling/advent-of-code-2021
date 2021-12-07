class Position:
    FORWARD = "forward"
    DOWN = "down"
    UP = "up"

    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def move(self, direction, amount):
        if direction == self.FORWARD:
            self.horizontal += amount
            self.depth += self.aim * amount
        if direction == self.DOWN:
            self.aim += amount
        if direction == self.UP:
            self.aim -= amount

    def multiply_position(self):
        return self.horizontal * self.depth
