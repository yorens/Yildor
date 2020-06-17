import random
class Deck:
    def __init__(self):
        self.deck = []

    def add_card(self, card):
        self.deck.append(card)

    def remove_card(self, input_card):
        for card in self.deck:
            if card == input_card:
                self.deck.remove(input_card)

    def contains(self, input_card):
        for card in self.deck:
            if card == input_card:
                return True
        return False
    
    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_card(self):
        if len(self.deck) == 0:
            return None
        card = self.deck[0]
        del self.deck[0]
        return card
                
    def length(self):
        return len(self.deck)