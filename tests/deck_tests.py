import card
import deck
import unittest
import yildor

class TestDeckMethods(unittest.TestCase):

    def test_deck_remove_card(self):
        deck_1 = deck.Deck()
        card_1 = card.Card(1, 0, yildor.sapphire, 2, 2, 1, 0, 0)
        card_2 = card.Card(1, 0, yildor.emerald, 2, 0, 1, 0, 2)
        card_3 = card.Card(1, 0, yildor.diamond, 2, 0, 1, 0, 2)
        deck_1.add_card(card_1)
        deck_1.add_card(card_2)
        deck_1.remove_card(card_2)
        self.assertTrue(deck_1.contains(card_1))
        self.assertFalse(deck_1.contains(card_2))
        self.assertFalse(deck_1.contains(card_3))

    def test_deck_deal_one_card(self):
        deck_1 = deck.Deck()
        card_1 = card.Card(1, 0, yildor.sapphire, 2, 2, 1, 0, 0)
        card_2 = card.Card(1, 0, yildor.emerald, 2, 0, 1, 0, 2)
        card_3 = card.Card(1, 0, yildor.diamond, 2, 0, 1, 0, 2)
        deck_1.add_card(card_1)
        deck_1.add_card(card_2)
        deck_1.add_card(card_3)
        self.assertTrue(deck_1.deal_card() == card_1)
        self.assertTrue(deck_1.deal_card() == card_2)

    def test_deck_deal_one_card_from_empty_deck(self):
        deck_1 = deck.Deck()
        self.assertTrue(deck_1.deal_card() == None)
        self.assertTrue(deck_1.deal_card() == None)



if __name__ == '__main__':
    unittest.main()
