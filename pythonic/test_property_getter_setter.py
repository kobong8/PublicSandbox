class Game:
    def __init__(self):
        self.__score = 0

    # getter
    def get_score(self):
        return self.__score
    
    # setter
    def set_score(self, value):
        self.__score = value


class GameWithProperty:
    def __init__(self):
        self.__score = 0

    # getter
    @ property    
    def score(self):
        return self.__score
    
    # setter
    @score.setter
    def score(self, value):
        self.__score = value


if __name__ == "__main__":
    print("Class without @property")
    tetris = Game()
    tetris.set_score(1000)
    print(f"tetris score: {tetris.get_score()}\n")

    print("Class without @property")
    tetris = GameWithProperty()
    tetris.score = 1000
    print(f"tetris score: {tetris.score}\n")
