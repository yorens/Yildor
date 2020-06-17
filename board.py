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
