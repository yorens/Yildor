import bank
import board
import card
import chip
import menu
import player
import random
import time
import yildor


class Game:
    def __init__(self):
        self.players = []
        self.current_player_number = 0
        # create decks
        self.turns = []
        random.seed()
        self.chip_storage = [0, 0, 0, 0, 0]

    def start(self):
        rank1 = all_rank_1_cards()
        rank2 = all_rank_2_cards()
        rank3 = all_rank_3_cards()
        rank4 = all_noble_cards()
        self.board = board.Board(
            rank1, rank2, rank3, rank4, bank.Bank(5, 5, 5, 5, 5))

    def get_num_players(self):
        return len(self.players)

    def debug_print(self, obj):
        print("*DEBUG*: " + str(obj))

    def debug_display(self):
        self.board.debug_display()

    def chip_storage_types_clear(self):
        self.chip_storage[0] = 0
        self.chip_storage[1] = 0
        self.chip_storage[2] = 0
        self.chip_storage[3] = 0
        self.chip_storage[4] = 0

    def create_first_menu(self):
        first_menu = menu.MenuChoiceInput("Do you want to...",
                               "Enter the number of your choice: ")
        first_menu.add_menu_item(menu.MenuItem("Start a new game", "c1", 1))
        first_menu.add_menu_item(menu.MenuItem("Exit", "c2", 2))
        first_menu.add_menu_item(menu.MenuItem("Get help", "c3", 3))
        return first_menu

    def ask_for_names(self):
        names = []
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
            names.append(player_name_menu.get_choice())
        return names

    def set_up_players(self, names):
        for name in names:
            self.players.append(player.Player(name))
        self.board.start(self.get_num_players())

    def create_turn_menu(self):
        turn_choice_menu = menu.MenuChoiceInput("Do you want to...",
                                "Enter the number of your choice:")
        self.debug_print(self.current_player())
        if self.current_player().total_num_chips() < 10:
            turn_choice_menu.add_menu_item(menu.MenuItem("Choose chips", "c1", 1))
        turn_choice_menu.add_menu_item(menu.MenuItem("Buy card", "c2", 2))
        turn_choice_menu.add_menu_item(
            menu.MenuItem("* display decks *", "c3", 3))
        turn_choice_menu.display()
        return turn_choice_menu
        
    def create_chip_choosing_menu(self):
        chip_choosing_menu = menu.MenuChoiceInput("", "Enter the number of your choice:")
        if self.board.bank.balance(yildor.diamond) == self.board.bank.max_num_diamond:
            chip_choosing_menu.add_menu_item(menu.MenuItem("Choose 2 " + yildor.diamond + "s", "A", 1))
        if self.board.bank.balance(yildor.sapphire) == self.board.bank.max_num_sapphire:
            chip_choosing_menu.add_menu_item(menu.MenuItem("Choose 2 " + yildor.sapphire + "s", "B", 2))
        if self.board.bank.balance(yildor.emerald) == self.board.bank.max_num_emerald:
            chip_choosing_menu.add_menu_item(menu.MenuItem("Choose 2 " + yildor.emerald + "s", "C", 3))
        if self.board.bank.balance(yildor.ruby) == self.board.bank.max_num_ruby:
            chip_choosing_menu.add_menu_item(menu.MenuItem("Choose 2 " + yildor.ruby + "s", "D", 4))
        if self.board.bank.balance(yildor.onyx) == self.board.bank.max_num_onyx:
            chip_choosing_menu.add_menu_item(menu.MenuItem("Choose 2 " + yildor.onyx + "s", "E", 5))
        if self.board.bank.balance(yildor.diamond) >= 0:
            chip_choosing_menu.add_menu_item(menu.MenuItem("Choose 1 " + yildor.diamond + "s", "F", 6))
        if self.board.bank.balance(yildor.sapphire) >= 0:
            chip_choosing_menu.add_menu_item(menu.MenuItem("Choose 1 " + yildor.sapphire + "s", "G", 7))
        if self.board.bank.balance(yildor.emerald) >= 0:
            chip_choosing_menu.add_menu_item(menu.MenuItem("Choose 1 " + yildor.emerald + "s", "H", 8))
        if self.board.bank.balance(yildor.ruby) >= 0:
            chip_choosing_menu.add_menu_item(menu.MenuItem("Choose 1 " + yildor.ruby + "s", "I", 9))
        if self.board.bank.balance(yildor.onyx) >= 0:
            chip_choosing_menu.add_menu_item(menu.MenuItem("Choose 1 " + yildor.onyx + "s", "J", 10))
        chip_choosing_menu.display()
        return chip_choosing_menu

    def current_player(self):
        return self.players[self.current_player_number]

    def play(self):
        while not self.is_game_over():
            self.board.display()
            turn_menu = self.create_turn_menu()
            if turn_menu.get_choice() == 1:
                choose_two = False
                x = 0
                while choose_two == False and x < 3:
                    chip_menu = self.create_chip_choosing_menu()
                    if chip_menu.get_menu_choice().function == "A":
                        self.chip_storage[0] = 2
                        choose_two = True
                    elif chip_menu.get_menu_choice().function == "B":
                        self.chip_storage[1] = 2
                        choose_two = True
                    elif chip_menu.get_menu_choice().function == "C":
                        self.chip_storage[2] = 2
                        choose_two = True
                    elif chip_menu.get_menu_choice().function == "D":
                        self.chip_storage[3] = 2
                        choose_two = True
                    elif chip_menu.get_menu_choice().function == "E":
                        self.chip_storage[4] = 2
                        choose_two = True
                    elif chip_menu.get_menu_choice().function == "F":
                        self.chip_storage[0] = 1
                        x += 1
                    elif chip_menu.get_menu_choice().function == "G":
                        self.chip_storage[1] = 1
                        x += 1
                    elif chip_menu.get_menu_choice().function == "H":
                        self.chip_storage[2] = 1
                        x += 1
                    elif chip_menu.get_menu_choice().function == "I":
                        self.chip_storage[3] = 1
                        x += 1
                    elif chip_menu.get_menu_choice().function == "J":
                        self.chip_storage[4] = 1
                        x += 1
                
            elif turn_menu.get_choice() == 2:
                print("Buying card")
            elif turn_menu.get_choice() == 3:
                self.board.debug_display()
            self.move_to_next_player()
        
    def is_game_over(self):
        return False

    def move_to_next_player(self):
        self.current_player_number += 1
        if self.current_player_number >= len(self.players):
            self.current_player_number = 0


def all_rank_1_cards():
    # return an array of all rank 1 cards
    cards = []
    cards.append(card.Card(1, 1, yildor.diamond, 0, 0, 4, 0, 0))
    cards.append(card.Card(1, 0, yildor.diamond, 0, 2, 0, 0, 2))
    cards.append(card.Card(1, 0, yildor.diamond, 0, 3, 0, 0, 0))
    cards.append(card.Card(1, 0, yildor.diamond, 0, 1, 1, 1, 1))
    cards.append(card.Card(1, 0, yildor.diamond, 0, 0, 0, 2, 1))
    cards.append(card.Card(1, 0, yildor.diamond, 0, 2, 2, 0, 1))
    cards.append(card.Card(1, 0, yildor.diamond, 0, 1, 2, 1, 1))
    cards.append(card.Card(1, 0, yildor.diamond, 3, 1, 0, 0, 1))
    cards.append(card.Card(1, 1, yildor.sapphire, 0, 0, 0, 4, 0))
    cards.append(card.Card(1, 0, yildor.sapphire, 1, 0, 0, 0, 2))
    cards.append(card.Card(1, 0, yildor.sapphire, 0, 0, 0, 0, 3))
    cards.append(card.Card(1, 0, yildor.sapphire, 1, 0, 1, 1, 1))
    cards.append(card.Card(1, 0, yildor.sapphire, 0, 0, 2, 0, 2))
    cards.append(card.Card(1, 0, yildor.sapphire, 1, 0, 2, 2, 0))
    cards.append(card.Card(1, 0, yildor.sapphire, 0, 1, 3, 1, 0))
    cards.append(card.Card(1, 0, yildor.sapphire, 1, 0, 1, 2, 1))
    cards.append(card.Card(1, 1, yildor.emerald, 0, 0, 0, 0, 4))
    cards.append(card.Card(1, 0, yildor.emerald, 0, 2, 0, 2, 0))
    cards.append(card.Card(1, 0, yildor.emerald, 0, 1, 0, 2, 2))
    cards.append(card.Card(1, 0, yildor.emerald, 2, 1, 0, 0, 0))
    cards.append(card.Card(1, 0, yildor.emerald, 1, 1, 0, 1, 1))
    cards.append(card.Card(1, 0, yildor.emerald, 1, 1, 0, 1, 2))
    cards.append(card.Card(1, 0, yildor.emerald, 0, 0, 0, 3, 0))
    cards.append(card.Card(1, 0, yildor.emerald, 1, 3, 1, 0, 0))
    cards.append(card.Card(1, 1, yildor.ruby, 4, 0, 0, 0, 0))
    cards.append(card.Card(1, 0, yildor.ruby, 2, 1, 1, 0, 1))
    cards.append(card.Card(1, 0, yildor.ruby, 3, 0, 0, 0, 0))
    cards.append(card.Card(1, 0, yildor.ruby, 1, 1, 1, 0, 1))
    cards.append(card.Card(1, 0, yildor.ruby, 2, 0, 1, 0, 2))
    cards.append(card.Card(1, 0, yildor.ruby, 0, 2, 1, 0, 0))
    cards.append(card.Card(1, 0, yildor.ruby, 2, 0, 0, 2, 0))
    cards.append(card.Card(1, 0, yildor.ruby, 1, 0, 0, 1, 3))
    cards.append(card.Card(1, 1, yildor.onyx, 0, 4, 0, 0, 0))
    cards.append(card.Card(1, 0, yildor.onyx, 1, 1, 1, 1, 0))
    cards.append(card.Card(1, 0, yildor.onyx, 0, 0, 3, 0, 0))
    cards.append(card.Card(1, 0, yildor.onyx, 1, 2, 1, 1, 0))
    cards.append(card.Card(1, 0, yildor.onyx, 0, 0, 1, 3, 1))
    cards.append(card.Card(1, 0, yildor.onyx, 0, 0, 2, 1, 0))
    cards.append(card.Card(1, 0, yildor.onyx, 2, 2, 0, 1, 0))
    cards.append(card.Card(1, 0, yildor.onyx, 2, 0, 2, 0, 0))
    return cards


def all_rank_2_cards():
    # return an array of all rank 2 cards
    cards = []
    cards.append(card.Card(2, 1, yildor.diamond, 2, 3, 0, 3, 0))
    cards.append(card.Card(2, 1, yildor.diamond, 0, 0, 3, 2, 2))
    cards.append(card.Card(2, 2, yildor.diamond, 0, 0, 1, 4, 2))
    cards.append(card.Card(2, 2, yildor.diamond, 0, 0, 0, 5, 3))
    cards.append(card.Card(2, 2, yildor.diamond, 0, 0, 0, 5, 0))
    cards.append(card.Card(2, 3, yildor.diamond, 6, 0, 0, 0, 0))
    cards.append(card.Card(2, 1, yildor.sapphire, 0, 2, 3, 0, 3))
    cards.append(card.Card(2, 1, yildor.sapphire, 0, 2, 2, 3, 0))
    cards.append(card.Card(2, 2, yildor.sapphire, 5, 3, 0, 0, 0))
    cards.append(card.Card(2, 2, yildor.sapphire, 2, 0, 0, 1, 4))
    cards.append(card.Card(2, 2, yildor.sapphire, 0, 5, 0, 0, 0))
    cards.append(card.Card(2, 3, yildor.sapphire, 0, 6, 0, 0, 0))
    cards.append(card.Card(2, 1, yildor.emerald, 2, 3, 0, 0, 2))
    cards.append(card.Card(2, 1, yildor.emerald, 3, 0, 2, 3, 0))
    cards.append(card.Card(2, 2, yildor.emerald, 4, 2, 0, 0, 1))
    cards.append(card.Card(2, 2, yildor.emerald, 0, 0, 5, 0, 0))
    cards.append(card.Card(2, 2, yildor.emerald, 0, 5, 3, 0, 0))
    cards.append(card.Card(2, 3, yildor.emerald, 0, 0, 6, 0, 0))
    cards.append(card.Card(2, 1, yildor.ruby, 2, 0, 0, 2, 3))
    cards.append(card.Card(2, 1, yildor.ruby, 0, 3, 0, 2, 3))
    cards.append(card.Card(2, 2, yildor.ruby, 1, 4, 2, 0, 0))
    cards.append(card.Card(2, 2, yildor.ruby, 3, 0, 0, 0, 5))
    cards.append(card.Card(2, 2, yildor.ruby, 0, 0, 0, 0, 5))
    cards.append(card.Card(2, 3, yildor.ruby, 0, 0, 0, 6, 0))
    cards.append(card.Card(2, 1, yildor.onyx, 3, 0, 3, 0, 2))
    cards.append(card.Card(2, 1, yildor.onyx, 3, 2, 2, 0, 0))
    cards.append(card.Card(2, 2, yildor.onyx, 0, 1, 4, 2, 0))
    cards.append(card.Card(2, 2, yildor.onyx, 5, 0, 0, 0, 0))
    cards.append(card.Card(2, 2, yildor.onyx, 0, 0, 5, 3, 0))
    cards.append(card.Card(2, 3, yildor.onyx, 0, 0, 0, 0, 6))
    return cards


def all_rank_3_cards():
    # return an array of all rank 3 cards
    cards = []
    cards.append(card.Card(3, 3, yildor.diamond, 0, 3, 3, 5, 3))
    cards.append(card.Card(3, 4, yildor.diamond, 3, 0, 0, 3, 6))
    cards.append(card.Card(3, 4, yildor.diamond, 0, 0, 0, 0, 7))
    cards.append(card.Card(3, 5, yildor.diamond, 3, 0, 0, 0, 7))
    cards.append(card.Card(3, 3, yildor.sapphire, 3, 0, 3, 3, 5))
    cards.append(card.Card(3, 4, yildor.sapphire, 6, 3, 0, 0, 3))
    cards.append(card.Card(3, 4, yildor.sapphire, 7, 0, 0, 0, 0))
    cards.append(card.Card(3, 5, yildor.sapphire, 7, 3, 0, 0, 0))
    cards.append(card.Card(3, 3, yildor.emerald, 5, 3, 0, 3, 3))
    cards.append(card.Card(3, 4, yildor.emerald, 3, 6, 3, 0, 0))
    cards.append(card.Card(3, 4, yildor.emerald, 0, 7, 0, 0, 0))
    cards.append(card.Card(3, 5, yildor.emerald, 0, 7, 3, 0, 0))
    cards.append(card.Card(3, 3, yildor.ruby, 3, 5, 3, 0, 3))
    cards.append(card.Card(3, 4, yildor.ruby, 0, 0, 7, 0, 0))
    cards.append(card.Card(3, 4, yildor.ruby, 0, 3, 6, 3, 0))
    cards.append(card.Card(3, 5, yildor.ruby, 0, 0, 7, 3, 0))
    cards.append(card.Card(3, 3, yildor.onyx, 3, 3, 5, 3, 0))
    cards.append(card.Card(3, 4, yildor.onyx, 0, 0, 0, 7, 0))
    cards.append(card.Card(3, 4, yildor.onyx, 0, 0, 3, 6, 3))
    cards.append(card.Card(3, 5, yildor.onyx, 0, 0, 0, 7, 3))
    return cards


def all_noble_cards():
    # return an array of all noble cards
    cards = []
    cards.append(card.Card(4, 3, yildor.noble, 3, 0, 0, 3, 3))
    cards.append(card.Card(4, 3, yildor.noble, 0, 3, 3, 3, 0))
    cards.append(card.Card(4, 3, yildor.noble, 3, 3, 0, 0, 3))
    cards.append(card.Card(4, 3, yildor.noble, 0, 0, 3, 3, 3))
    cards.append(card.Card(4, 3, yildor.noble, 3, 3, 3, 0, 0))
    cards.append(card.Card(4, 3, yildor.noble, 0, 0, 4, 4, 0))
    cards.append(card.Card(4, 3, yildor.noble, 4, 0, 0, 0, 4))
    cards.append(card.Card(4, 3, yildor.noble, 4, 4, 0, 0, 0))
    cards.append(card.Card(4, 3, yildor.noble, 0, 0, 0, 4, 4))
    cards.append(card.Card(4, 3, yildor.noble, 0, 4, 4, 0, 0))
    return cards


if __name__ == '__main__':
    game = Game()
    first_menu = game.create_first_menu()
    first_menu.display()
    if first_menu.get_choice() == 2:
        print("Ok, Goodbye.")
        quit()
    elif first_menu.get_choice() == 3:
        print("[INSERT RULES FOR SPLENDOR HERE]")
    else:
        print("Ok, you chose to start a new game.")
        game.start()
        names = game.ask_for_names()
        game.set_up_players(names)
        game.play()
