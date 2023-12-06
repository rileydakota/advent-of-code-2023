class Grid:
    def __init__(self, raw_data: str):
        split = raw_data.split("\n")
        self.data = [[char for char in line] for line in split]
        self.width = len(self.data)
        self.height = len(self.data[0])

    def set(self, x, y, value):
        self.data[y][x] = value

    def get(self, x, y):
        try:
            return self.data[y][x]
        except IndexError as e:
            return None

    def get_below(self, x, y):
        try:
            return self.data[y + 1][x]
        except IndexError as e:
            return None

    def get_above(self, x, y):
        if y - 1 < 0:
            return None

        try:
            return self.data[y - 1][x]
        except IndexError as e:
            return None

    def get_diag_left_below(self, x, y):
        if x - 1 < 0:
            return None

        try:
            return self.data[y + 1][x - 1]
        except IndexError as e:
            return None

    def get_diag_right_below(self, x, y):
        try:
            return self.data[y + 1][x + 1]
        except IndexError as e:
            return None

    def get_diag_right_above(self, x, y):
        if y - 1 < 0:
            return None

        try:
            return self.data[y - 1][x + 1]
        except IndexError as e:
            return None

    def get_diag_left_above(self, x, y):
        if y - 1 < 0 or x - 1 < 0:
            return None

        try:
            return self.data[y - 1][x - 1]
        except IndexError as e:
            return None


class EngineSchematic:
    def __init__(self, raw_schematic: str):
        self.raw_schematic = raw_schematic
        self.grid = Grid(self.raw_schematic)
