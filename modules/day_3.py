SYMBOLS = ['$', '+', '@', '-', '=', '#', '&', '*', '/', '%']

class SchematicInteger:
    def __init__(self, val, x, y):
        self.x = x
        self.y = y
        self.val = val

    def __str__(self):
        return f'"x": {self.x}, "y": {self.y}, "val": {self.val}'
    
    def __repr__(self):
        return f"SchematicInteger({self.x}, {self.y}, {self.val})"

class SchematicNumber:
    def __init__(self):
        self.integers = []
    
    
    def add_integer(self, integer):
        self.integers.append(integer)

    def is_part_number(self, grid):
        
        all_surrounding = []

        for num in self.integers:
            surrounding = list(grid.get_surrounding_chars(num.x, num.y).values())
            all_surrounding = surrounding + all_surrounding

        return set(all_surrounding) & set(SYMBOLS)

    def get_integer(self):
        return int("".join([x.val for x in self.integers]))



class EngineSchematic:
    def __init__(self, raw_data: str):
        split = raw_data.split("\n")
        self.data = [[char for char in line] for line in split]
        self.width = len(self.data)
        self.height = len(self.data[0])
        self.numbers = self.get_numbers()
        self.part_numbers = self.get_part_numbers()

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

    def get_left(self, x, y):
        if x - 1 < 0:
            return None
        try:
            return self.data[y][x - 1]
        except IndexError as e:
            return None
    
    def get_right(self, x, y):
        try:
            return self.data[y][x + 1]
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
    
    def get_surrounding_chars(self, x, y):
        return {
            "up": self.get_above(x, y),
            "down": self.get_below(x, y),
            "left": self.get_left(x, y),
            "right": self.get_right(x, y),
            "diag_bottom_left": self.get_diag_left_below(x, y),
            "diag_bottom_right": self.get_diag_right_below(x, y),
            "diag_upper_left": self.get_diag_left_above(x, y),
            "diag_upper_right": self.get_diag_right_above(x, y)
        }
    
    def get_part_numbers(self):
        return [x.get_integer() for x in self.numbers if x.is_part_number(self)]
    
    def get_part_number_sum(self):
        return sum(self.part_numbers)

    def get_numbers(self):

        writing_num = False
        numbers = []
        current_number = None


        for y in range(0, self.width):
            if current_number:
                numbers.append(current_number)
                writing_num = False
                current_number = None

            for x in range(0, self.height):
                cursor = self.get(x, y)
                if cursor is not None:
                    if cursor.isnumeric() and writing_num == False:
                        current_number = SchematicNumber() 
                        current_number.add_integer(SchematicInteger(cursor, x, y))
                        writing_num = True
                    
                    elif cursor.isnumeric() and writing_num == True:
                        current_number.add_integer(SchematicInteger(cursor, x, y))

                    elif not cursor.isnumeric() and writing_num == True:
                        numbers.append(current_number)
                        writing_num = False
                        current_number = None
                    else:
                        continue
        return numbers
    

def solve_part_1(input) -> int:
    schematic = EngineSchematic(input)
    return schematic.get_part_number_sum()




