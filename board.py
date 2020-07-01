import bank
import deck
import random

class Board:
    def __init__(self, rank_1_deck=None, rank_2_deck=None, rank_3_deck=None, noble_deck=None, game_bank=None):
        if rank_1_deck is None:
            self.rank_1_deck = deck.Deck(None)
        else:
            self.rank_1_deck = deck.Deck(rank_1_deck)

        if rank_2_deck is None:
            self.rank_2_deck = deck.Deck(None)
        else:
            self.rank_2_deck = deck.Deck(rank_2_deck)

        if rank_3_deck is None:
            self.rank_3_deck = deck.Deck(None)
        else:
            self.rank_3_deck = deck.Deck(rank_3_deck)

        if noble_deck is None:
            self.noble_deck = deck.Deck(None)
        else:
            self.noble_deck = deck.Deck(noble_deck)

        if game_bank is None:
            self.bank = bank.Bank(0, 0, 0, 0, 0)
        else:
            self.bank = game_bank

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

        for _ in range(num_players + 1):
            self.noble_cards_deployed.append(self.noble_deck.deal_card())

    def display(self):
        NobleRowOfSevenLines(self.noble_cards_deployed).print_row()
        RowOfSevenLines(self.rank_3_cards_deployed).print_row()
        RowOfSevenLines(self.rank_2_cards_deployed).print_row()
        RowOfSevenLines(self.rank_1_cards_deployed).print_row()

    def debug_display(self):
        # break the deck into rows of four
        print("********************************************************* DEBUG ********************************************************* ")
        d = []
        print("rank 1 deck:")
        print(self.rank_1_deck)
        for card in self.rank_1_deck:
            print(card)
            d.append(card)
            if len(d) == 4:
                RowOfSevenLines(d).print_row()
                d = []
        if len(d) > 0:
            RowOfSevenLines(d).print_row()

        d = []
        print("rank 2 deck:")
        print(self.rank_2_deck)
        for card in self.rank_2_deck:
            print(card)
            d.append(card)
            if len(d) == 4:
                RowOfSevenLines(d).print_row()
                d = []
        if len(d) > 0:
            RowOfSevenLines(d).print_row()
        d = []
        print("rank 3 deck:")
        print(self.rank_3_deck)
        for card in self.rank_3_deck:
            print(card)
            d.append(card)
            if len(d) == 4:
                RowOfSevenLines(d).print_row()
                d = []
        if len(d) > 0:
            RowOfSevenLines(d).print_row()
        d = []
        print("noble deck:")
        print(self.noble_deck)
        # force a four and three card row
        displayedFour = False
        displayedThree = False
        for c in self.noble_deck:
            print(c)
            d.append(c)
            if len(d) == 4 and not displayedFour:
                NobleRowOfSevenLines(d).print_row()
                displayedFour = True
                d = []
            elif len(d) == 3 and not displayedThree:
                NobleRowOfSevenLines(d).print_row()
                displayedThree = True
                d = []
        # there are three more cards, use None to force a 5 card row
        d.append(None)
        d.append(None)
        if len(d) > 0:
            NobleRowOfSevenLines(d).print_row()
        print("********************************************************* DEBUG ********************************************************* ")

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
        card_number = 1
        rank = self.cards[0].get_rank()
        if rank == 1:
            card_number = 9
        elif rank == 2:
            card_number = 5

        buffer = ""
        for card in self.cards:
            if card != self.cards[0]:
                buffer += "      "
            buffer += "| {0:1} Onyx(s) {1:13}|".format(
                card.cost_onyx(), card_number)
            card_number += 1
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
            elif length <= 3:
                if card != self.cards[0]:
                    buffer += "                         "
                buffer += "┌──────────────────────┐"
        return buffer

    def row_1(self):
        buffer = ""
        length = len(self.cards)
        for card in self.cards:
            point = "X"
            gem_type = "noble"
            if card is not None:
                point = str(card.get_point_value())
                gem_type = card.get_gem_type()

            if length == 5:
                spaces = 13
                if card != self.cards[0]:
                    buffer += "   "
                buffer += "| " + point + (" " * spaces) + gem_type+"|"
            if length == 4:
                spaces = 17
                if card != self.cards[0]:
                    buffer += "      "
                buffer += "| " + point + (" " * spaces) + gem_type+"|"
            if length <= 3:
                spaces = 15
                if card != self.cards[0]:
                    buffer += "                         "
                buffer += "| " + point + (" " * spaces) + gem_type+"|"
        return buffer

    def row_2(self):
        buffer = ""
        length = len(self.cards)
        for card in self.cards:
            rank = "X"
            if card is not None:
                rank = str(card.get_rank())

            if length == 5:
                if card != self.cards[0]:
                    buffer += "   " 
                buffer += "|        Rank "+rank+"      |"
            if length == 4:
                if card != self.cards[0]:
                    buffer += "      " 
                buffer += "|        Rank "+rank+"          |"
            if length <= 3:
                if card != self.cards[0]:
                    buffer += "                         " 
                buffer += "|        Rank "+rank+"        |"
        return buffer

    def row_3(self):
        buffer = ""
        length = len(self.cards)
        for card in self.cards:
            cost = "X"
            if card is not None:
                cost = str(card.cost_diamond())

            if length == 5:
                if card != self.cards[0]:
                    buffer += "   " 
                buffer += "| "+cost+" Diamond(s)       |"
            if length == 4:
                if card != self.cards[0]:
                    buffer += "      " 
                buffer += "| "+cost+" Diamond(s)           |"
            if length <= 3:
                if card != self.cards[0]:
                    buffer += "                         " 
                buffer += "| "+cost+" Diamond(s)         |"
        return buffer

    def row_4(self):
        buffer  = ""
        length = len(self.cards)
        for card in self.cards:
            cost = "X"
            if card is not None:
                cost = str(card.cost_sapphire())

            if length == 5:
                if card != self.cards[0]:
                    buffer += "   " 
                buffer += "| "+cost+" Sapphire(s)      |"
            if length == 4:
                if card != self.cards[0]:
                    buffer += "      " 
                buffer += "| "+cost+" Sapphire(s)          |"
            if length <= 3:
                if card != self.cards[0]:
                    buffer += "                         " 
                buffer += "| "+cost+" Sapphire(s)        |"
        return buffer

    def row_5(self):
        buffer  = ""
        length = len(self.cards)
        for card in self.cards:
            cost = "X"
            if card is not None:
                cost = str(card.cost_emerald())

            if length == 5:
                if card != self.cards[0]:
                    buffer += "   " 
                buffer += "| "+cost+" Emerald(s)       |"
            if length == 4:
                if card != self.cards[0]:
                    buffer += "      " 
                buffer += "| "+cost+" Emerald(s)           |"
            if length <= 3:
                if card != self.cards[0]:
                    buffer += "                         " 
                buffer += "| "+cost+" Emerald(s)         |"
        return buffer

    def row_6(self):
        buffer  = ""
        length = len(self.cards)
        for card in self.cards:
            cost = "X"
            if card is not None:
                cost = str(card.cost_ruby())
            if length == 5:
                if card != self.cards[0]:
                    buffer += "   " 
                buffer += "| "+cost+" Ruby(s)          |"
            if length == 4:
                if card != self.cards[0]:
                    buffer += "      " 
                buffer += "| "+cost+" Ruby(s)              |"
            if length <= 3:
                if card != self.cards[0]:
                    buffer += "                         " 
                buffer += "| "+cost+" Ruby(s)            |"
        return buffer

    def row_7(self):
        buffer = ""
        length = len(self.cards)
        for card in self.cards:
            cost = "X"
            if card is not None:
                cost = card.cost_onyx()
            if length == 5:
                if card != self.cards[0]:
                    buffer += "   "
                buffer += "| {0:1} Onyx(s)  {1:8}|".format(cost, " ")
            if length == 4:
                if card != self.cards[0]:
                    buffer += "      "
                buffer += "| {0:1} Onyx(s) {1:13}|".format(cost, " ")
            if length <= 3:
                if card != self.cards[0]:
                    buffer += "                         "
                buffer += "| {0:1} Onyx(s) {1:11}|".format(cost, " ")
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
            elif length <= 3:
                if card != self.cards[0]:
                    buffer += "                         "
                buffer += "└──────────────────────┘"

        return buffer
