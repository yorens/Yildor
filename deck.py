import card
import random


class Deck:
    def __init__(self, cards=None):
        if cards is None:
            self.cards = []
        else:
            self.cards = cards

    def __repr__(self):
        buffer = "{size: " + str(len(self.cards)) + "\n"
        if len(self.cards) > 0:
            for card in self.cards:
                buffer += " " + str(card) + "\n"

        buffer += "}"
        return buffer

    def __str__(self):
        buffer = "Deck(size=" + str(len(self.cards)) + "\n"
        if len(self.cards) > 0:
            for card in self.cards:
                buffer += " " + str(card) + "\n"

        buffer += ")"
        return buffer

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, input_card):
        for card in self.cards:
            if card == input_card:
                self.cards.remove(input_card)

    def contains(self, input_card):
        for card in self.cards:
            if card == input_card:
                return True
        return False

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) == 0:
            return None
        card = self.cards[0]
        del self.cards[0]
        return card

    def length(self):
        return len(self.cards)
