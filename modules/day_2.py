class Game():
    def __init__(self, game_str:str):
        self.game_str = game_str
        self.id = self.__get_game_id(self.game_str)
    
    def __get_game_id(self, game_str:str):
        return int(game_str.split(':')[0].split(' ')[1])

    def __parse_game_string(self, game_str:str):
        sets_text = game_str.split(': ')[1].split(';')
        for set_text in sets_text:
            cubes = set_text.split(',')

            
