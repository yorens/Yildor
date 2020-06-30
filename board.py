import bank
import card
import deck
import random


class Board:
    def __init__(self, rank_1_deck=None, rank_2_deck=None, rank_3_deck=None, noble_deck=None, bank=None):
        if rank_1_deck == None:
            self.rank_1_deck = deck.Deck(None)
        else:
            self.rank_1_deck = deck.Deck(rank_1_deck)
        if rank_2_deck == None:
            self.rank_2_deck = deck.Deck(None)
        else:
            self.rank_2_deck = deck.Deck(rank_2_deck)
        if rank_3_deck == None:
            self.rank_3_deck = deck.Deck(None)
        else:
            self.rank_3_deck = deck.Deck(rank_3_deck)
        if noble_deck == None:
            self.noble_deck = deck.Deck(None)
        else:
            self.noble_deck = deck.Deck(noble_deck)

        if bank == None:
            self.bank = bank.Bank(0, 0, 0, 0, 0)
        else:
            self.bank = bank
        self.rank_1_cards_deployed = []
        self.rank_2_cards_deployed = []
        self.rank_3_cards_deployed = []
        self.noble_cards_deployed = []

    # TODO method created to demonstrate capturing printed
    # output for testing purposes
    def print_top_line(self):
        print("------")

    def start(self, num_players):
        self.rank_1_deck.shuffle_deck()
        self.rank_2_deck.shuffle_deck()
        self.rank_3_deck.shuffle_deck()
        self.noble_deck.shuffle_deck()
        self.rank_1_cards_deployed.append(self.rank_1_deck.deal_card())
        self.rank_1_cards_deployed.append(self.rank_1_deck.deal_card())
        self.rank_1_cards_deployed.append(self.rank_1_deck.deal_card())
        self.rank_1_cards_deployed.append(self.rank_1_deck.deal_card())
        self.rank_2_cards_deployed.append(self.rank_2_deck.deal_card())
        self.rank_2_cards_deployed.append(self.rank_2_deck.deal_card())
        self.rank_2_cards_deployed.append(self.rank_2_deck.deal_card())
        self.rank_2_cards_deployed.append(self.rank_2_deck.deal_card())
        self.rank_3_cards_deployed.append(self.rank_3_deck.deal_card())
        self.rank_3_cards_deployed.append(self.rank_3_deck.deal_card())
        self.rank_3_cards_deployed.append(self.rank_3_deck.deal_card())
        self.rank_3_cards_deployed.append(self.rank_3_deck.deal_card())

        for i in range(num_players + 1):
            self.noble_cards_deployed.append(self.noble_deck.deal_card())

    def display(self):
        NobleRowOfSevenLines(self.noble_cards_deployed).print_row()
        RowOfSevenLines(self.rank_3_cards_deployed).print_row()
        RowOfSevenLines(self.rank_2_cards_deployed).print_row()
        RowOfSevenLines(self.rank_1_cards_deployed).print_row()



# RowOfSevenLines prints a row of 1-4 cards
# in seven lines.
# example:
#   card_1 = card.Card(1, 9, yildor.sapphire).set_cost_diamond(1).set_cost_sapphire(2).set_cost_emerald(3).set_cost_ruby(4).set_cost_onyx(5)
#   card_2 = card.Card(1, 9, yildor.emerald).set_cost_diamond(1).set_cost_sapphire(2).set_cost_emerald(3).set_cost_ruby(4).set_cost_onyx(5)
#   card_3 = card.Card(1, 9, yildor.ruby).set_cost_diamond(1).set_cost_sapphire(2).set_cost_emerald(3).set_cost_ruby(4).set_cost_onyx(5)
#   card_4 = card.Card(1, 9, yildor.diamond).set_cost_diamond(1).set_cost_sapphire(2).set_cost_emerald(3).set_cost_ruby(4).set_cost_onyx(5)
#   board.RowOfSevenLines([card_1, card_2, card_3, card_4]).print_row()
#   board.RowOfSevenLines([card_1, card_2, card_3]).print_row()
#   board.RowOfSevenLines([card_1, card_2]).print_row()
#   board.RowOfSevenLines([card_1]).print_row()
class RowOfSevenLines:
    def __init__(self, cards=[]):
        self.cards = cards

    def print_row(self):
        print(self.row_header())
        print(self.row_1())
        print(self.row_2())
        print(self.row_3())
        print(self.row_4())
        print(self.row_5())
        print(self.row_6())
        print(self.row_7())
        print(self.row_footer())

    def row_header(self):
        buffer = ""
        for i in range(len(self.cards)):
            if i > 0:
                buffer += "      "
            buffer += "┌────────────────────────┐"
        return buffer

    def row_1(self):
        buffer = ""
        for card in self.cards:
            spaces = 22
            if card != self.cards[0]:
                buffer += "      " 
            gem_type = card.get_gem_type()
            spaces -= len(gem_type)
            buffer += "| "+str(card.get_point_value()) + (" " * spaces) +gem_type+"|"
        return buffer

    def row_2(self):
        buffer = ""
        for card in self.cards:
            if card != self.cards[0]:
                buffer += "      " 
            buffer += "|        Rank "+str(card.get_rank())+"          |"
        return buffer

    def row_3(self):
        buffer = ""
        for card in self.cards:
            if card != self.cards[0]:
                buffer += "      " 
            buffer += "| "+str(card.cost_diamond())+" Diamond(s)           |"
        return buffer

    def row_4(self):
        buffer = ""
        for card in self.cards:
            if card != self.cards[0]:
                buffer += "      " 
            buffer += "| "+str(card.cost_sapphire())+" Sapphire(s)          |"
        return buffer

    def row_5(self):
        buffer = ""
        for card in self.cards:
            if card != self.cards[0]:
                buffer += "      " 
            buffer += "| "+str(card.cost_emerald())+" Emerald(s)           |"
        return buffer

    def row_6(self):
        buffer = ""
        for card in self.cards:
            if card != self.cards[0]:
                buffer += "      " 
            buffer += "| "+str(card.cost_ruby())+" Ruby(s)              |"
        return buffer

    def row_7(self):
        buffer = ""
        for card in self.cards:
            if card != self.cards[0]:
                buffer += "      " 
            buffer += "| "+str(card.cost_onyx())+" Onyx(s)              |"
        return buffer

    def row_footer(self):
        buffer = ""
        for i in range(len(self.cards)):
            if i > 0:
                buffer += "      "
            buffer += "└────────────────────────┘"
        return buffer

# NobleRowOfSevenLines prints a row of 1-5 noble cards
# in seven lines.
# example:
#   n1 = card.Card(4, 9, yildor.noble).set_cost_diamond(1).set_cost_sapphire(2).set_cost_emerald(3).set_cost_ruby(4).set_cost_onyx(5)
#   n2 = card.Card(4, 9, yildor.noble).set_cost_diamond(1).set_cost_sapphire(2).set_cost_emerald(3).set_cost_ruby(4).set_cost_onyx(5)
#   n3 = card.Card(4, 9, yildor.noble).set_cost_diamond(1).set_cost_sapphire(2).set_cost_emerald(3).set_cost_ruby(4).set_cost_onyx(5)
#   n4 = card.Card(4, 9, yildor.noble).set_cost_diamond(1).set_cost_sapphire(2).set_cost_emerald(3).set_cost_ruby(4).set_cost_onyx(5)
#   n5 = card.Card(4, 9, yildor.noble).set_cost_diamond(1).set_cost_sapphire(2).set_cost_emerald(3).set_cost_ruby(4).set_cost_onyx(5)
#   board.NobleRowOfSevenLines([n1, n2, n3, n4, n5]).print_row()
#   board.NobleRowOfSevenLines([n1, n2, n3, n4]).print_row()
#   board.NobleRowOfSevenLines([n1, n2, n3]).print_row()
class NobleRowOfSevenLines:
    def __init__(self, cards=[]):
        self.cards = cards

    def print_row(self):
        print(self.row_header())
        print(self.row_1())
        print(self.row_2())
        print(self.row_3())
        print(self.row_4())
        print(self.row_5())
        print(self.row_6())
        print(self.row_7())
        print(self.row_footer())

    def row_header(self):
        buffer = ""
        length = len(self.cards)
        for card in self.cards:
            if length == 5:
                if card != self.cards[0]:
                    buffer += "   "
                buffer += "┌────────────────────┐"
            elif length == 4:
                if card != self.cards[0]:
                    buffer += "      "
                buffer += "┌────────────────────────┐"
            elif length == 3:
                if card != self.cards[0]:
                    buffer += "                         "
                buffer += "┌──────────────────────┐"
        return buffer

    def row_1(self):
        buffer = ""
        length = len(self.cards)
        for card in self.cards:
            if length == 5:
                spaces = 13
                if card != self.cards[0]:
                    buffer += "   "
                buffer += "| " + str(card.get_point_value()) + (" " * spaces) + card.get_gem_type()+"|"
            if length == 4:
                spaces = 17
                if card != self.cards[0]:
                    buffer += "      "
                buffer += "| " + str(card.get_point_value()) + (" " * spaces) + card.get_gem_type()+"|"
            if length == 3:
                spaces = 15
                if card != self.cards[0]:
                    buffer += "                         "
                buffer += "| " + str(card.get_point_value()) + (" " * spaces) + card.get_gem_type()+"|"
        return buffer

    def row_2(self):
        buffer = ""
        length = len(self.cards)
        for card in self.cards:
            if length == 5:
                if card != self.cards[0]:
                    buffer += "   " 
                buffer += "|        Rank "+str(card.get_rank())+"      |"
            if length == 4:
                if card != self.cards[0]:
                    buffer += "      " 
                buffer += "|        Rank "+str(card.get_rank())+"          |"
            if length == 3:
                if card != self.cards[0]:
                    buffer += "                         " 
                buffer += "|        Rank "+str(card.get_rank())+"        |"
        return buffer

    def row_3(self):
        buffer = ""
        length = len(self.cards)
        for card in self.cards:
            if length == 5:
                if card != self.cards[0]:
                    buffer += "   " 
                buffer += "| "+str(card.cost_diamond())+" Diamond(s)       |"
            if length == 4:
                if card != self.cards[0]:
                    buffer += "      " 
                buffer += "| "+str(card.cost_diamond())+" Diamond(s)           |"
            if length == 3:
                if card != self.cards[0]:
                    buffer += "                         " 
                buffer += "| "+str(card.cost_diamond())+" Diamond(s)         |"
        return buffer

    def row_4(self):
        buffer  = ""
        length = len(self.cards)
        for card in self.cards:
            if length == 5:
                if card != self.cards[0]:
                    buffer += "   " 
                buffer += "| "+str(card.cost_sapphire())+" Sapphire(s)      |"
            if length == 4:
                if card != self.cards[0]:
                    buffer += "      " 
                buffer += "| "+str(card.cost_sapphire())+" Sapphire(s)          |"
            if length == 3:
                if card != self.cards[0]:
                    buffer += "                         " 
                buffer += "| "+str(card.cost_sapphire())+" Sapphire(s)        |"
        return buffer

    def row_5(self):
        buffer  = ""
        length = len(self.cards)
        for card in self.cards:
            if length == 5:
                if card != self.cards[0]:
                    buffer += "   " 
                buffer += "| "+str(card.cost_emerald())+" Emerald(s)       |"
            if length == 4:
                if card != self.cards[0]:
                    buffer += "      " 
                buffer += "| "+str(card.cost_emerald())+" Emerald(s)           |"
            if length == 3:
                if card != self.cards[0]:
                    buffer += "                         " 
                buffer += "| "+str(card.cost_emerald())+" Emerald(s)         |"
        return buffer

    def row_6(self):
        buffer  = ""
        length = len(self.cards)
        for card in self.cards:
            if length == 5:
                if card != self.cards[0]:
                    buffer += "   " 
                buffer += "| "+str(card.cost_ruby())+" Ruby(s)          |"
            if length == 4:
                if card != self.cards[0]:
                    buffer += "      " 
                buffer += "| "+str(card.cost_ruby())+" Ruby(s)              |"
            if length == 3:
                if card != self.cards[0]:
                    buffer += "                         " 
                buffer += "| "+str(card.cost_ruby())+" Ruby(s)            |"
        return buffer

    def row_7(self):
        buffer  = ""
        length = len(self.cards)
        for card in self.cards:
            if length == 5:
                if card != self.cards[0]:
                    buffer += "   " 
                buffer += "| "+str(card.cost_onyx())+" Onyx(s)          |"
            if length == 4:
                if card != self.cards[0]:
                    buffer += "      " 
                buffer += "| "+str(card.cost_onyx())+" Onyx(s)              |"
            if length == 3:
                if card != self.cards[0]:
                    buffer += "                         " 
                buffer += "| "+str(card.cost_onyx())+" Onyx(s)            |"
        return buffer

    def row_footer(self):
        buffer = ""
        length = len(self.cards)
        for card in self.cards:
            if length == 5:
                if card != self.cards[0]:
                    buffer += "   "
                buffer += "└────────────────────┘"
            elif length == 4:
                if card != self.cards[0]:
                    buffer += "      "
                buffer += "└────────────────────────┘"
            elif length == 3:
                if card != self.cards[0]:
                    buffer += "                         "
                buffer += "└──────────────────────┘"

        return buffer
