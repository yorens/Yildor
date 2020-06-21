import random
import menu
import player


class Game:
    def __init__(self):
        self.players = []
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
        first_menu = menu.Menu("Do you want to...",
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
        for p in self.players:
            print(p.to_string())

    # def create_second_menu(self):
    #     second_menu = menu.Menu("Hp", "o")


if __name__ == '__main__':
    game = Game()
    game.set_up_players()
    # first_menu = game.create_first_menu()
    # first_menu.display()
    # if first_menu.choice == "2":
    #     print("Ok, Goodbye.")
    #     quit()
    # else:
    #     print("Ok, you chose to start a new game.")
    #     game.start()
