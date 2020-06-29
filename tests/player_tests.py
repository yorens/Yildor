import card
import chip
import player
import unittest
import yildor


class TestPlayerMethods(unittest.TestCase):

    def test_player_one_diamond_card(self):
        player_1 = player.Player("Yildiz")
        diamond = card.Card(1, 0, yildor.diamond, 2, 2, 1, 0, 0)
        player_1.add_card(diamond)
        self.assertTrue(player_1.diamond_cards_currently() == 1)
        self.assertTrue(player_1.sapphire_cards_currently() == 0)
        self.assertTrue(player_1.emerald_cards_currently() == 0)
        self.assertTrue(player_1.ruby_cards_currently() == 0)
        self.assertTrue(player_1.onyx_cards_currently() == 0)
    
    def test_player_one_sapphire_card(self):
        player_1 = player.Player("Yildiz")
        sapphire = card.Card(1, 0, yildor.sapphire, 2, 2, 1, 0, 0)
        player_1.add_card(sapphire)
        self.assertTrue(player_1.diamond_cards_currently() == 0)
        self.assertTrue(player_1.sapphire_cards_currently() == 1)
        self.assertTrue(player_1.emerald_cards_currently() == 0)
        self.assertTrue(player_1.ruby_cards_currently() == 0)
        self.assertTrue(player_1.onyx_cards_currently() == 0)
    
    def test_player_one_emerald_card(self):
        player_1 = player.Player("Yildiz")
        emerald = card.Card(1, 0, yildor.emerald, 2, 2, 1, 0, 0)
        player_1.add_card(emerald)
        self.assertTrue(player_1.diamond_cards_currently() == 0)
        self.assertTrue(player_1.sapphire_cards_currently() == 0)
        self.assertTrue(player_1.emerald_cards_currently() == 1)
        self.assertTrue(player_1.ruby_cards_currently() == 0)
        self.assertTrue(player_1.onyx_cards_currently() == 0)
    
    def test_player_one_ruby_card(self):
        player_1 = player.Player("Yildiz")
        ruby = card.Card(1, 0, yildor.ruby, 2, 2, 1, 0, 0)
        player_1.add_card(ruby)
        self.assertTrue(player_1.diamond_cards_currently() == 0)
        self.assertTrue(player_1.sapphire_cards_currently() == 0)
        self.assertTrue(player_1.emerald_cards_currently() == 0)
        self.assertTrue(player_1.ruby_cards_currently() == 1)
        self.assertTrue(player_1.onyx_cards_currently() == 0)
    
    def test_player_one_onyx_card(self):
        player_1 = player.Player("Yildiz")
        onyx = card.Card(1, 0, yildor.onyx, 2, 2, 1, 0, 0)
        player_1.add_card(onyx)
        self.assertTrue(player_1.diamond_cards_currently() == 0)
        self.assertTrue(player_1.sapphire_cards_currently() == 0)
        self.assertTrue(player_1.emerald_cards_currently() == 0)
        self.assertTrue(player_1.ruby_cards_currently() == 0)
        self.assertTrue(player_1.onyx_cards_currently() == 1)

    def test_player_two_cards(self):
        player_1 = player.Player("Yildiz")
        player_1.add_card(card.Card(1, 0, yildor.onyx, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.diamond, 2, 2, 1, 0, 0))
        self.assertTrue(player_1.diamond_cards_currently() == 1)
        self.assertTrue(player_1.sapphire_cards_currently() == 0)
        self.assertTrue(player_1.emerald_cards_currently() == 0)
        self.assertTrue(player_1.ruby_cards_currently() == 0)
        self.assertTrue(player_1.onyx_cards_currently() == 1)

    def test_player_three_cards(self):
        player_1 = player.Player("Yildiz")
        player_1.add_card(card.Card(1, 0, yildor.onyx, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.diamond, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.ruby, 2, 2, 1, 0, 0))
        self.assertTrue(player_1.diamond_cards_currently() == 1)
        self.assertTrue(player_1.sapphire_cards_currently() == 0)
        self.assertTrue(player_1.emerald_cards_currently() == 0)
        self.assertTrue(player_1.ruby_cards_currently() == 1)
        self.assertTrue(player_1.onyx_cards_currently() == 1)

    def test_player_four_cards(self):
        player_1 = player.Player("Yildiz")
        player_1.add_card(card.Card(1, 0, yildor.onyx, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.diamond, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.ruby, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.emerald, 2, 2, 1, 0, 0))
        self.assertTrue(player_1.diamond_cards_currently() == 1)
        self.assertTrue(player_1.sapphire_cards_currently() == 0)
        self.assertTrue(player_1.emerald_cards_currently() == 1)
        self.assertTrue(player_1.ruby_cards_currently() == 1)
        self.assertTrue(player_1.onyx_cards_currently() == 1)

    def test_player_five_cards(self):
        player_1 = player.Player("Yildiz")
        player_1.add_card(card.Card(1, 0, yildor.onyx, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.diamond, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.ruby, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.emerald, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.sapphire, 2, 2, 1, 0, 0))
        self.assertTrue(player_1.diamond_cards_currently() == 1)
        self.assertTrue(player_1.sapphire_cards_currently() == 1)
        self.assertTrue(player_1.emerald_cards_currently() == 1)
        self.assertTrue(player_1.ruby_cards_currently() == 1)
        self.assertTrue(player_1.onyx_cards_currently() == 1)

    def test_player_two_diamond_cards(self):
        player_1 = player.Player("Yildiz")
        player_1.add_card(card.Card(1, 0, yildor.onyx, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.diamond, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.diamond, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.ruby, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.emerald, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.sapphire, 2, 2, 1, 0, 0))
        self.assertTrue(player_1.diamond_cards_currently() == 2)
        self.assertTrue(player_1.sapphire_cards_currently() == 1)
        self.assertTrue(player_1.emerald_cards_currently() == 1)
        self.assertTrue(player_1.ruby_cards_currently() == 1)
        self.assertTrue(player_1.onyx_cards_currently() == 1)

    def test_player_add_one_diamond_chip(self):
        player_1 = player.Player("Yildiz")
        chip_1 = chip.Chip(yildor.diamond)
        player_1.add_chip(chip_1)

    def test_player_add_one_sapphire_chip(self):
        player_1 = player.Player("Yildiz")
        chip_1 = chip.Chip(yildor.sapphire)
        player_1.add_chip(chip_1)

    def test_player_add_one_emerald_chip(self):
        player_1 = player.Player("Yildiz")
        chip_1 = chip.Chip(yildor.emerald)
        player_1.add_chip(chip_1)

    def test_player_add_one_ruby_chip(self):
        player_1 = player.Player("Yildiz")
        chip_1 = chip.Chip(yildor.ruby)
        player_1.add_chip(chip_1)

    def test_player_add_one_onyx_chip(self):
        player_1 = player.Player("Yildiz")
        chip_1 = chip.Chip(yildor.onyx)
        player_1.add_chip(chip_1)

    def test_player_remove_one_diamond_chip_when_chips(self):
        player_1 = player.Player("Yildiz")
        chip_1 = chip.Chip(yildor.diamond)
        player_1.add_chip(chip_1)
        player_1.add_chip(chip_1)
        self.assertTrue(player_1.diamond_chips == 2)
        player_1.remove_chip(chip_1)
        self.assertTrue(player_1.diamond_chips == 1)

    def test_player_remove_one_diamond_chip_when_no_chips(self):
        player_1 = player.Player("Yildiz")
        chip_1 = chip.Chip(yildor.diamond)
        player_1.remove_chip(chip_1)
        self.assertTrue(player_1.diamond_chips == 0)

    def test_player_total_chips(self):
        player_1 = player.Player("Yildiz")
        player_1.add_chip(chip.Chip(yildor.diamond))
        player_1.add_chip(chip.Chip(yildor.sapphire))
        player_1.add_chip(chip.Chip(yildor.emerald))
        player_1.add_chip(chip.Chip(yildor.ruby))
        player_1.add_chip(chip.Chip(yildor.onyx))
        self.assertTrue(player_1.total_num_chips() == 5)

if __name__ == '__main__':
    unittest.main()
