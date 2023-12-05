class ScratchCard:
    def __init__(self, card_str: str):
        self.card_str = card_str
        self.card_id = self.__get_card_id(self.card_str)
        self.__parse_card_string(self.card_str)

    def __get_card_id(self, card_str: str):
        try:
            return card_str.split(":")[0].split(" ")[1]
        except Exception as e:
            print(f"failed to parse card. raw string: {card_str}")
            raise e

    def __parse_card_string(self, card_str: str):
        try:
            card_nums_split = card_str.split(":")[1].split("|")
            winning_nums = card_nums_split[0].lstrip().rstrip().split(" ")
            card_nums = card_nums_split[1].lstrip().rstrip().split(" ")

            winning_nums = remove_items(winning_nums, "")
            card_nums = remove_items(card_nums, "")

            self.winning_nums = list(map(lambda n: int(n), winning_nums))
            self.card_nums = list(map(lambda n: int(n), card_nums))
        except Exception as e:
            print(f"failed to parse card. raw string: {card_str}")
            raise e

    def get_winning_numbers(self) -> list:
        actual_winning_numbers = []
        for win_num in self.winning_nums:
            if win_num in self.card_nums:
                actual_winning_numbers.append(win_num)
        return actual_winning_numbers

    def get_point_value(self) -> int:
        win_num_count = len(self.get_winning_numbers())

        if win_num_count == 0 or win_num_count == 1:
            return win_num_count
        else:
            point_val = 1
            for x in range(1, win_num_count):
                point_val = point_val * 2
            return point_val


def remove_items(list, item):
    # using list comprehension to perform the task
    res = [i for i in list if i != item]
    return res


def solve_part_1(input: str):
    cards = [ScratchCard(x) for x in input.split("\n")]

    total = 0

    for card in cards:
        total += card.get_point_value()

    return total
