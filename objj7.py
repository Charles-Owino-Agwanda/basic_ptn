class ScoreBoard:
    def __init__(self, score):
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, new_score):
        if new_score > 0:
            self.__score = new_score

    def get_score(self):
        return self.__score


s1 = ScoreBoard(0)
print(s1.score)
s1.score = 30
print(s1.score)
