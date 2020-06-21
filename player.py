import card
import chip
import yildor
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

    def to_string(self):
        return "<player name: " + self.name + ">"
        
    def emerald_cards_currently(self):
        return len(self.emerald_cards)
    
    def diamond_cards_currently(self):
        return len(self.diamond_cards)

    def sapphire_cards_currently(self):
        return len(self.sapphire_cards)

    def ruby_cards_currently(self):
        return len(self.ruby_cards)

    def onyx_cards_currently(self):
        return len(self.onyx_cards)

    def emerald_chips_currently(self):
        return self.emerald_chips
    
    def diamond_chips_currently(self):
        return self.diamond_chips

    def sapphire_chips_currently(self):
        return self.sapphire_chips

    def ruby_chips_currently(self):
        return self.ruby_chips

    def onyx_chips_currently(self):
        return self.onyx_chips

    def add_card(self, card):
        card_type = card.gem_type
        if card_type == yildor.diamond:
            self.diamond_cards.append(card)

        elif card_type == yildor.sapphire:
            self.sapphire_cards.append(card)

        elif card_type == yildor.emerald:
            self.emerald_cards.append(card)
        
        elif card_type == yildor.ruby:
            self.ruby_cards.append(card)

        elif card_type == yildor.onyx:
            self.onyx_cards.append(card)

    def add_chip(self, chip):
        chip_type = chip.gem_type
        if chip_type == yildor.diamond:
            self.diamond_chips += 1

        elif chip_type == yildor.sapphire:
            self.sapphire_chips += 1

        elif chip_type == yildor.emerald:
            self.emerald_chips += 1
        
        elif chip_type == yildor.ruby:
            self.ruby_chips += 1

        elif chip_type == yildor.onyx:
            self.onyx_chips += 1

    def remove_chip(self, chip):
        chip_type = chip.gem_type
        if chip_type == yildor.diamond:
            self.diamond_chips -= 1
            if self.diamond_chips <= 0:
                self.diamond_chips = 0
                return 0
            return 1

        elif chip_type == yildor.sapphire:
            self.sapphire_chips -= 1
            if self.sapphire_chips <= 0:
                self.sapphire_chips = 0
                return 0
            return 1

        elif chip_type == yildor.emerald:
            self.emerald_chips -= 1
            if self.emerald_chips <= 0:
                self.emerald_chips = 0
                return 0
            return 1
        
        elif chip_type == yildor.ruby:
            self.ruby_chips -= 1
            if self.ruby_chips <= 0:
                self.ruby_chips = 0
                return 0
            return 1

        elif chip_type == yildor.onyx:
            self.onyx_chips -= 1
            if self.onyx_chips <= 0:
                self.onyx_chips = 0
                return 0
            return 1