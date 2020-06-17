import card
import player
import unittest
import yildor


class TestPlayerMethods(unittest.TestCase):

    def test_one_diamond_card(self):
        player_1 = player.Player("Yildiz")
        diamond = card.Card(1, 0, yildor.diamond, 2, 2, 1, 0, 0)
        player_1.add_card(diamond)
        self.assertTrue(player_1.diamond_card_buying() == 1)
        self.assertTrue(player_1.sapphire_card_buying() == 0)
        self.assertTrue(player_1.emerald_card_buying() == 0)
        self.assertTrue(player_1.ruby_card_buying() == 0)
        self.assertTrue(player_1.onyx_card_buying() == 0)
    
    def test_one_sapphire_card(self):
        player_1 = player.Player("Yildiz")
        sapphire = card.Card(1, 0, yildor.sapphire, 2, 2, 1, 0, 0)
        player_1.add_card(sapphire)
        self.assertTrue(player_1.diamond_card_buying() == 0)
        self.assertTrue(player_1.sapphire_card_buying() == 1)
        self.assertTrue(player_1.emerald_card_buying() == 0)
        self.assertTrue(player_1.ruby_card_buying() == 0)
        self.assertTrue(player_1.onyx_card_buying() == 0)
    
    def test_one_emerald_card(self):
        player_1 = player.Player("Yildiz")
        emerald = card.Card(1, 0, yildor.emerald, 2, 2, 1, 0, 0)
        player_1.add_card(emerald)
        self.assertTrue(player_1.diamond_card_buying() == 0)
        self.assertTrue(player_1.sapphire_card_buying() == 0)
        self.assertTrue(player_1.emerald_card_buying() == 1)
        self.assertTrue(player_1.ruby_card_buying() == 0)
        self.assertTrue(player_1.onyx_card_buying() == 0)
    
    def test_one_ruby_card(self):
        player_1 = player.Player("Yildiz")
        ruby = card.Card(1, 0, yildor.ruby, 2, 2, 1, 0, 0)
        player_1.add_card(ruby)
        self.assertTrue(player_1.diamond_card_buying() == 0)
        self.assertTrue(player_1.sapphire_card_buying() == 0)
        self.assertTrue(player_1.emerald_card_buying() == 0)
        self.assertTrue(player_1.ruby_card_buying() == 1)
        self.assertTrue(player_1.onyx_card_buying() == 0)
    
    def test_one_onyx_card(self):
        player_1 = player.Player("Yildiz")
        onyx = card.Card(1, 0, yildor.onyx, 2, 2, 1, 0, 0)
        player_1.add_card(onyx)
        self.assertTrue(player_1.diamond_card_buying() == 0)
        self.assertTrue(player_1.sapphire_card_buying() == 0)
        self.assertTrue(player_1.emerald_card_buying() == 0)
        self.assertTrue(player_1.ruby_card_buying() == 0)
        self.assertTrue(player_1.onyx_card_buying() == 1)

    def test_two_cards(self):
        player_1 = player.Player("Yildiz")
        player_1.add_card(card.Card(1, 0, yildor.onyx, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.diamond, 2, 2, 1, 0, 0))
        self.assertTrue(player_1.diamond_card_buying() == 1)
        self.assertTrue(player_1.sapphire_card_buying() == 0)
        self.assertTrue(player_1.emerald_card_buying() == 0)
        self.assertTrue(player_1.ruby_card_buying() == 0)
        self.assertTrue(player_1.onyx_card_buying() == 1)

    def test_three_cards(self):
        player_1 = player.Player("Yildiz")
        player_1.add_card(card.Card(1, 0, yildor.onyx, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.diamond, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.ruby, 2, 2, 1, 0, 0))
        self.assertTrue(player_1.diamond_card_buying() == 1)
        self.assertTrue(player_1.sapphire_card_buying() == 0)
        self.assertTrue(player_1.emerald_card_buying() == 0)
        self.assertTrue(player_1.ruby_card_buying() == 1)
        self.assertTrue(player_1.onyx_card_buying() == 1)

    def test_four_cards(self):
        player_1 = player.Player("Yildiz")
        player_1.add_card(card.Card(1, 0, yildor.onyx, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.diamond, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.ruby, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.emerald, 2, 2, 1, 0, 0))
        self.assertTrue(player_1.diamond_card_buying() == 1)
        self.assertTrue(player_1.sapphire_card_buying() == 0)
        self.assertTrue(player_1.emerald_card_buying() == 1)
        self.assertTrue(player_1.ruby_card_buying() == 1)
        self.assertTrue(player_1.onyx_card_buying() == 1)

    def test_five_cards(self):
        player_1 = player.Player("Yildiz")
        player_1.add_card(card.Card(1, 0, yildor.onyx, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.diamond, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.ruby, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.emerald, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.sapphire, 2, 2, 1, 0, 0))
        self.assertTrue(player_1.diamond_card_buying() == 1)
        self.assertTrue(player_1.sapphire_card_buying() == 1)
        self.assertTrue(player_1.emerald_card_buying() == 1)
        self.assertTrue(player_1.ruby_card_buying() == 1)
        self.assertTrue(player_1.onyx_card_buying() == 1)

    def test_two_diamond_cards(self):
        player_1 = player.Player("Yildiz")
        player_1.add_card(card.Card(1, 0, yildor.onyx, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.diamond, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.diamond, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.ruby, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.emerald, 2, 2, 1, 0, 0))
        player_1.add_card(card.Card(1, 0, yildor.sapphire, 2, 2, 1, 0, 0))
        self.assertTrue(player_1.diamond_card_buying() == 2)
        self.assertTrue(player_1.sapphire_card_buying() == 1)
        self.assertTrue(player_1.emerald_card_buying() == 1)
        self.assertTrue(player_1.ruby_card_buying() == 1)
        self.assertTrue(player_1.onyx_card_buying() == 1)


if __name__ == '__main__':
    unittest.main()
