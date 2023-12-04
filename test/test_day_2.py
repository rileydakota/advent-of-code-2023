from modules import day_2

def test_game():

    input = "Game 15: 4 red, 5 blue, 4 green; 7 red, 8 blue, 2 green; 9 blue, 6 red; 1 green, 3 red, 7 blue; 3 green, 7 red"

    game = day_2.Game(input)
    assert game.id == 15
    assert len(game.sets) == 5
    assert game.sets[0].red == 4
    assert game.sets[0].blue == 5
    assert game.sets[0].green == 4

    assert game.sets[2].red == 6
    assert game.sets[2].blue == 9
    assert game.sets[2].green == 0


def test_is_game_possible():

    input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    game = day_2.Game(input)

    assert day_2.is_game_possible(red=12, green=13, blue=14, game=game) == True

    input = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
    game = day_2.Game(input)

    assert day_2.is_game_possible(red=12, green=13, blue=14, game=game) == True

    input = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    game = day_2.Game(input)

    assert day_2.is_game_possible(red=12, green=13, blue=14, game=game) == False

    input = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
    game = day_2.Game(input)

    assert day_2.is_game_possible(red=12, green=13, blue=14, game=game) == False

    input = "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    game = day_2.Game(input)

    assert day_2.is_game_possible(red=12, green=13, blue=14, game=game) == True

def test_get_min_cubes():

    input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    game = day_2.Game(input)
    min_cubes = day_2.get_min_cubes(game)

    assert min_cubes.red == 4 and min_cubes.green == 2 and min_cubes.blue == 6

def test_example_input():

    input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

    assert day_2.solve_part_1(input) == 8
    
    


