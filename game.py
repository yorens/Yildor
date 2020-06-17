import random

class Game:
    def __init__(self, num_players):
        self.num_players = num_players
        #create decks
        #create bank
        #create players
        #create board
        self.turns = []
        random.seed()

    def start(self):
        print("game started")

if __name__ == '__main__':
    game = Game(1)
    game.start()
