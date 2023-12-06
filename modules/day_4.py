class ScratchCardManager:
    def __init__(self, card_array: list):
        self.card_array = card_array
        self.card_dict = {}

        for card in self.card_array:
            self.card_dict[card.card_id] = {"copies": 1, "card": card}

    def copy_card(self, card_id: int):
        self.card_dict[card_id]["copies"] += 1

    def win_cards(self, win_card_id: int, win_num_count: int):
        win_card_increment = win_card_id + 1
        for x in range(0, win_num_count):
            self.copy_card(win_card_increment)
            win_card_increment += 1

    def get_card(self, card_id):
        return self.card_dict[card_id]["card"]

    def eval_all_cards(self):
        for card_id in self.card_dict.keys():
            card = self.get_card(card_id)
            self.win_cards(card_id, len(card.get_winning_numbers()))
            if self.card_dict[card_id]["copies"] > 1:
                for x in range(1, self.card_dict[card_id]["copies"]):
                    winning_num_count = len(
                        self.get_card(card_id).get_winning_numbers()
                    )
                    if winning_num_count > 0:
                        self.win_cards(card_id, winning_num_count)

    def get_total_cards(self):
        count = 0
        for card_id in self.card_dict.keys():
            count += self.card_dict[card_id]["copies"]
        return count


class ScratchCard:
    def __init__(self, card_str: str):
        self.card_str = card_str
        self.card_id = self.__get_card_id(self.card_str)
        self.__parse_card_string(self.card_str)

    def __str__(self):
        return f"Card ID: {self.card_id} Winning Numbers: {self.winning_nums} Card Numbers {self.card_nums} Matching Numbers: {self.get_winning_numbers()}"

    def __get_card_id(self, card_str: str):
        try:
            split = card_str.split(":")[0].split(" ")
            split_clean = remove_items(split, "")
            return int(split_clean[1])
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


def solve_part_2(input: str):
    cards = [ScratchCard(x) for x in input.split("\n")]

    manager = ScratchCardManager(cards)
    manager.eval_all_cards()
    return manager.get_total_cards()
