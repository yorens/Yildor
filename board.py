class Board:
    def __init__(self, rank_1_deck=[], rank_2_deck=[], rank_3_deck=[], noble_deck=[], bank=[]):
        self.rank_1_deck = rank_1_deck
        self.rank_2_deck = rank_2_deck
        self.rank_3_deck = rank_3_deck
        self.noble_deck = noble_deck
        self.bank = bank

    # TODO method created to demonstrate capturing printed
    # output for testing purposes
    def print_top_line(self):
        print("------")

# RowOfSevenLines prints a row of 1-4 cards
# in seven lines.
# example:
#   card_1 = card.Card(1, 9, yildor.sapphire).set_cost_diamond(1).set_cost_sapphire(2).set_cost_emerald(3).set_cost_ruby(4).set_cost_onyx(5)
#   card_2 = card.Card(1, 9, yildor.emerald).set_cost_diamond(1).set_cost_sapphire(2).set_cost_emerald(3).set_cost_ruby(4).set_cost_onyx(5)
#   card_3 = card.Card(1, 9, yildor.ruby).set_cost_diamond(1).set_cost_sapphire(2).set_cost_emerald(3).set_cost_ruby(4).set_cost_onyx(5)
#   card_4 = card.Card(1, 9, yildor.diamond).set_cost_diamond(1).set_cost_sapphire(2).set_cost_emerald(3).set_cost_ruby(4).set_cost_onyx(5)
#   r = board.RowOfSevenLines([card_1, card_2, card_4])
#   r.print_row()
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
