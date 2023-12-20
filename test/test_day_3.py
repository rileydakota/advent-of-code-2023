from modules import day_3

def test_get_gear_ratios():
    input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    grid = day_3.EngineSchematic(raw_data=input)

    assert grid.numbers[0].x == {0,1,2}
    assert grid.numbers[0].y == {0,0,0}
    assert grid.gear_symbols[0].x == 3
    assert grid.gear_symbols[0].y == 1

    assert len(grid.gear_symbols) == 3
    assert day_3.are_adjacent(grid.gear_symbols[0], grid.numbers[0])
    assert day_3.are_adjacent(grid.gear_symbols[2], grid.numbers[0]) == False
    assert day_3.are_adjacent(grid.gear_symbols[2], grid.numbers[1]) == False
    assert day_3.are_adjacent(grid.gear_symbols[1], grid.numbers[4])

    assert len(grid.gear_symbols[0].adjacent_numbers) == 2
    assert len(grid.gear_symbols[2].adjacent_numbers) == 2
    assert len(grid.gear_ratios) == 2

    assert grid.gear_ratios == [16345, 451490]
    assert sum(grid.gear_ratios) == 467835




def test_get_numbers():
    input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    grid = day_3.EngineSchematic(raw_data=input)
    numbers = grid.get_numbers()
    assert numbers[0].integers[0].x == 0
    assert numbers[0].integers[0].y == 0
    assert len(numbers) == 10
    assert numbers[0].get_integer() == 467
    assert numbers[1].get_integer() == 114
    assert len(grid.part_numbers) == 8

    assert grid.part_numbers == [467, 35, 633, 617, 592, 755, 664, 598]

    assert grid.get_part_number_sum() == 4361

def test_grid():
    input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    grid = day_3.EngineSchematic(raw_data=input)

    assert grid.get(0, 0) == "4"
    assert grid.get_below(0, 0) == "."
    assert grid.get_above(0, 0) == None
    assert grid.get_diag_right_above(0, 0) == None
    assert grid.get_diag_left_above(0, 0) == None

    assert grid.get(2, 2) == "3"
    assert grid.get_diag_right_above(2, 2) == "*"

    assert grid.get(6, 9) == "9"

    assert grid.get(2, 0) == "7"
    assert grid.get_diag_right_below(2, 0) == "*"

    assert grid.get(6, 2) == "6"
    assert grid.get_below(6, 2) == "#"

    assert grid.get(9, 9) == "."
    assert grid.get_diag_left_below(9, 9) == None
    assert grid.get_diag_right_below(9, 9) == None

    assert grid.width == 10
    assert grid.height == 10
