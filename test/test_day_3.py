from modules import day_3


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

    grid = day_3.Grid(raw_data=input)

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
