class ScratchCard()
    def __init__(self, card_str:str):
        self.card_str = card_str
        self.card_id = self.__get_card_id(self.card_str)
        self.__parse_card_string(self.card_str)
    
    def __get_card_id(self, card_str:str):
        try: 
            return card_str.split(':')[0].split(' ')[1]
        except Exception as e:
            print(f"failed to parse card. raw string: {card_str}")
            raise e

    def __parse_card_string(self, card_str:str):
        try:
            card_nums_split = card_str.split(':')[1].split('|')
            winning_nums = card_nums_split[0].lstrip().split(' ')
            card_nums = card_nums_split[1].lstrip().split(' ')

            self.winning_nums = list(map(lambda n: int(n), winning_nums))
            self.self.card_nums = list(map(lambda n: int(n), winning_nums))