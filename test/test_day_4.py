from modules import day_4


def test_scratch_card():
    input = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"

    card = day_4.ScratchCard(input)
    output = ["48", "83", "17", "86"]

    assert len(output) == len(card.get_winning_numbers())
    assert 8 == card.get_point_value()


def test_solve():
    input = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"

    answer = day_4.solve_part_1(input)
    assert answer == 8
