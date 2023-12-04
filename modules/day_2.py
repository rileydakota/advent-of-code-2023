class Set():
    def __init__(self, red:int=0, green:int=0, blue:int=0):
        self.red=red
        self.green=green
        self.blue=blue
    
    def __str__(self):
        return f"red: {self.red}, green: {self.green}, blue: {self.blue}"

class Game():
    def __init__(self, game_str:str):
        self.game_str = game_str
        self.id = self.__get_game_id(self.game_str)
        self.sets = self.__parse_game_string(self.game_str)
    
    def __get_game_id(self, game_str:str):
        return int(game_str.split(':')[0].split(' ')[1])

    def __parse_game_string(self, game_str:str):
        sets_text = game_str.split(': ')[1].split(';')
        res = []
        for set_text in sets_text:
            game_set = Set()
            cubes = set_text.split(',')
            for cube in cubes:
                cube = cube.lstrip()
                split = cube.split(' ')
                try:
                    color = split[1].lower()
                    count = int(split[0])
                except Exception as e:
                    raise e
                match color:
                    case 'red':
                        game_set.red = count
                    case 'blue':
                        game_set.blue = count
                    case 'green':
                        game_set.green = count
            res.append(game_set)
        return res

    def __iter__(self):
        return iter(self.sets)
    def __str__(self):
        return self.game_str
    
def is_game_possible(red, green, blue, game) -> bool:
    reds = []
    greens = []
    blues = []


    for game_set in game:
        reds.append(game_set.red)
        blues.append(game_set.blue)
        greens.append(game_set.green)
    
    return ( red >= max(reds) and green >= max(greens) and blue >= max(blues) )

def get_min_cubes(game) -> Set:
    reds = []
    greens = []
    blues = []

    for game_set in game:
        reds.append(game_set.red)
        blues.append(game_set.blue)
        greens.append(game_set.green)

    return Set(red=max(reds), green=max(greens), blue=max(blues))

def solve_part_1(input) -> int:
    games_raw = input.split('\n')
    games = []
    for game_raw in games_raw:
        games.append(Game(game_raw))
    possible_games = []
    for game in games:
        if is_game_possible(red=12, green=13, blue=14, game=game):
            possible_games.append(game)  
    res = 0

    for game in possible_games:
        res += game.id

    return res

def solve_part_2(input) -> int:
    games_raw = input.split('\n')
    games = []
    for game_raw in games_raw:
        games.append(Game(game_raw))

    res = 0
    for game in games:
        min_cubes = get_min_cubes(game)
        power = min_cubes.red * min_cubes.green * min_cubes.blue
        res += power
    
    return res

