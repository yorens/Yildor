class Deck:
    def __init__(self):
        self.deck = []

    def add_card(self, card):
        self.deck.append(card)

    def remove_card_from_deck(self, input_card):
        for card in self.deck:
            if card == input_card:
                self.deck.remove(input_card)

    def contains(self, input_card):
        for card in self.deck:
            if card == input_card:
                return True
        return False
                