from modules import day_3

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
