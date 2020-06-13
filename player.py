import card

class Player:
    def __init__(self, name):
        self.number = -1
        self.name = name
        self.diamond_chips = 0
        self.sapphire_chips = 0
        self.emerald_chips = 0
        self.ruby_chips = 0
        self.onyx_chips = 0
        self.diamond_cards = []
        self.sapphire_cards = []
        self.emerald_cards = []
        self.ruby_cards = []
        self.onyx_cards = []
        self.wild_tokens = 0
        
    def emerald_card_buying(self):
        return len(self.emerald_cards)
    
    def diamond_card_buying(self):
        return len(self.diamond_cards)

    def sapphire_card_buying(self):
        return len(self.sapphire_cards)

    def ruby_card_buying(self):
        return len(self.ruby_cards)

    def onyx_card_buying(self):
        return len(self.onyx_cards)

    def emerald_chip_buying(self):
        return self.emerald_chips
    
    def diamond_chip_buying(self):
        return self.diamond_chips

    def sapphire_chip_buying(self):
        return self.sapphire_chips

    def ruby_chip_buying(self):
        return self.ruby_chips

    def onyx_chip_buying(self):
        return self.onyx_chips

    def add_card(self, card):
        card_type = card.gem_type
        if card_type == "diamond":
            self.diamond_cards.append(card)

        elif card_type == "sapphire":
            self.sapphire_cards.append(card)

        elif card_type == "emerald":
            self.emerald_cards.append(card)
        
        elif card_type == "ruby":
            self.ruby_cards.append(card)

        elif card_type == "onyx":
            self.onyx_cards.append(card)

