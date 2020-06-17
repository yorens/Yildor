import card
import deck
import unittest
import yildor

class TestDeckMethods(unittest.TestCase):

    def test_remove_card_from_deck(self):
        deck_1 = deck.Deck()
        card_1 = card.Card(1, 0, yildor.sapphire, 2, 2, 1, 0, 0)
        deck_1.add_card(card_1)
        card_2 = card.Card(1, 0, yildor.emerald, 2, 0, 1, 0, 2)
        deck_1.add_card(card_2)
        # card_3 = card.Card(1, 0, yildor.diamond, 2, 0, 1, 0, 2)
        deck_1.remove_card_from_deck(card_2)
        self.assertTrue(deck_1.contains(card_1))


if __name__ == '__main__':
    unittest.main()
