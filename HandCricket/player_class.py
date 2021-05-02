'''
Class to store the Player related details like
Name, Score, Target
'''


class Player():
    def __init__(self, name, score=0, target=0, play=False, wicket=False):
        self.name = name
        self.score = score
        self.target = target
        self.play = play
        self.wicket = wicket

    def add_score(self, score):
        self.score += score

    def check_if_win(self):
        if self.score > self.target:
            return "Yes"
        elif self.score == self.target:
            return "Tie"
        else:
            return "No"
