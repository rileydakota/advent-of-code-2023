from modules import day_4

def test_card_manager():
    input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

    card_array = []
    for line in input.split('\n'):
        card_array.append(day_4.ScratchCard(line))

    card_manager = day_4.ScratchCardManager(card_array)

    card_manager.win_cards(1, 4)
    assert card_manager.card_dict[2]['copies'] == 2

    card_manager = day_4.ScratchCardManager(card_array)
    res = card_manager.eval_all_cards()
    print(card_manager.card_dict)
    assert res == 30



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
