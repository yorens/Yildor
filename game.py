import random
import menu
import player
import time
import chip
import yildor


class Game:
    def __init__(self):
        self.players = []
        self.current_player_number = 0
        # create decks
        # create bank
        # create players
        # create board
        self.turns = []
        random.seed()

    def start(self):
        print("game started")

    def get_num_players(self):
        return len(self.players)

    def display(self, string):
        print(string)

    def create_first_menu(self):
        first_menu = menu.MenuChoiceInput("Do you want to...",
                               "Enter the number of your choice: ")
        first_menu.add_menu_item(menu.MenuItem("Start a new game", "c1", 1))
        first_menu.add_menu_item(menu.MenuItem("Exit", "c2", 2))
        return first_menu

    def set_up_players(self):
        player_menu = menu.MenuIntegerInput(
            "", "How many players are playing (please enter a number)? ")
        player_menu.display()
        num_players_input = player_menu.get_choice()
        while num_players_input < 2 or num_players_input > 4:
            print("Sorry, this time enter a number from 2 to 4.")
            player_menu.display()
            num_players_input = player_menu.get_choice()
        for i in range(num_players_input):
            player_name_menu = menu.MenuStringInput("",
                                                    "Enter the name for player " + str(i + 1) + ": ")
            player_name_menu.display()
            self.players.append(player.Player(player_name_menu.get_choice()))

        self.players[0].add_chip(chip.Chip(yildor.diamond))
        # print(self.players[0].to_string())
        self.players[0].add_chip(chip.Chip(yildor.diamond))
        self.players[0].add_chip(chip.Chip(yildor.diamond))
        self.players[0].add_chip(chip.Chip(yildor.diamond))
        self.players[0].add_chip(chip.Chip(yildor.diamond))
        self.players[0].add_chip(chip.Chip(yildor.diamond))
        self.players[0].add_chip(chip.Chip(yildor.diamond))
        self.players[0].add_chip(chip.Chip(yildor.diamond))
        self.players[0].add_chip(chip.Chip(yildor.diamond))
        self.players[0].add_chip(chip.Chip(yildor.diamond))
        # print(self.players[0].to_string())
        # for p in self.players:
        #     print(p.to_string())


    # def create_second_menu(self):
    #     second_menu = menu.Menu("Hp", "o")

    def create_turn_menu(self):
        turn_choice_menu = menu.MenuChoiceInput("Do you want to...",
                                "Enter the number of your choice:")
        print(self.current_player().to_string())
        if self.current_player().total_num_chips() < 10:
            turn_choice_menu.add_menu_item(menu.MenuItem("Choose chips", "c1", 1))
        turn_choice_menu.add_menu_item(menu.MenuItem("Buy card", "c2", 2))
        turn_choice_menu.display()
        return turn_choice_menu

    def current_player(self):
        return self.players[self.current_player_number]

    def play(self):
        while not self.is_game_over():
            turn_menu = self.create_turn_menu()
            if turn_menu.get_choice() == 1:
                print("Choosing chips")
            elif turn_menu.get_choice() == 2:
                print("Buying card")
            self.move_to_next_player()
        
    def is_game_over(self):
        return False

    def move_to_next_player(self):
        self.current_player_number += 1
        if self.current_player_number >= len(self.players):
            self.current_player_number = 0


if __name__ == '__main__':
    game = Game()
    first_menu = game.create_first_menu()
    first_menu.display()
    if first_menu.get_choice() == 2:
        print("Ok, Goodbye.")
        quit()
    else:
        print("Ok, you chose to start a new game.")
        game.start()
        game.set_up_players()
        game.play()
