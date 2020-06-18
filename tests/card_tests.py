import unittest
import card
import yildor

class TestCardMethods(unittest.TestCase):

    def test_card_set_cost_diamond(self):
        card_1 = card.Card(1, 0, yildor.sapphire)
        card_1.set_cost_diamond(2)
        self.assertTrue(card_1.cost_diamond() == 2)

    def test_card_set_cost_diamond_in_constructor(self):
        card_1 = card.Card(1, 0, yildor.sapphire, 2)
        self.assertTrue(card_1.cost_diamond() == 2)

    def test_card_set_cost_sapphire(self):
        card_1 = card.Card(1, 0, yildor.sapphire)
        card_1.set_cost_sapphire(2)
        self.assertTrue(card_1.cost_sapphire() == 2)

    def test_card_set_cost_sapphire_in_constructor(self):
        card_1 = card.Card(1, 0, yildor.sapphire, 0, 2)
        self.assertTrue(card_1.cost_sapphire() == 2)

    def test_card_set_cost_emerald(self):
        card_1 = card.Card(1, 0, yildor.sapphire)
        card_1.set_cost_emerald(2)
        self.assertTrue(card_1.cost_emerald() == 2)

    def test_card_set_cost_emerald_in_constructor(self):
        card_1 = card.Card(1, 0, yildor.sapphire, 0, 0, 2)
        self.assertTrue(card_1.cost_emerald() == 2)

    def test_card_set_cost_ruby(self):
        card_1 = card.Card(1, 0, yildor.sapphire)
        card_1.set_cost_ruby(2)
        self.assertTrue(card_1.cost_ruby() == 2)

    def test_card_set_cost_ruby_in_constructor(self):
        card_1 = card.Card(1, 0, yildor.sapphire, 0, 0, 0, 2)
        self.assertTrue(card_1.cost_ruby() == 2)

    def test_card_set_cost_onyx(self):
        card_1 = card.Card(1, 0, yildor.sapphire)
        card_1.set_cost_onyx(2)
        self.assertTrue(card_1.cost_onyx() == 2)

    def test_card_set_cost_onyx_in_constructor(self):
        card_1 = card.Card(1, 0, yildor.sapphire, 0, 0, 0, 0, 2)
        self.assertTrue(card_1.cost_onyx() == 2)

    def test_card_set_multiple_costs_in_constructor(self):
        card_1 = card.Card(1, 0, yildor.sapphire, 1, 2, 3, 4, 5)
        self.assertTrue(card_1.cost_diamond() == 1)
        self.assertTrue(card_1.cost_sapphire() == 2)
        self.assertTrue(card_1.cost_emerald() == 3)
        self.assertTrue(card_1.cost_ruby() == 4)
        self.assertTrue(card_1.cost_onyx() == 5)

    def test_card_set_multiple_costs(self):
        card_1 = card.Card(1, 0, yildor.sapphire)
        card_1.set_cost_diamond(1).set_cost_sapphire(2).set_cost_emerald(3).set_cost_ruby(4).set_cost_onyx(5)
        self.assertTrue(card_1.cost_diamond() == 1)
        self.assertTrue(card_1.cost_sapphire() == 2)
        self.assertTrue(card_1.cost_emerald() == 3)
        self.assertTrue(card_1.cost_ruby() == 4)
        self.assertTrue(card_1.cost_onyx() == 5)

    def test_card_5_gem_cost(self):
        card_1 = card.Card(1, 0, yildor.sapphire)
        card_1.set_cost_diamond(1).set_cost_sapphire(2).set_cost_emerald(3).set_cost_ruby(4).set_cost_onyx(5)
        self.assertTrue(card_1.number_of_gem_costs() == 5)

    def test_card_4_gem_cost(self):
        card_1 = card.Card(1, 0, yildor.sapphire)
        card_1.set_cost_diamond(1).set_cost_sapphire(2).set_cost_emerald(3).set_cost_ruby(4)
        self.assertTrue(card_1.number_of_gem_costs() == 4)

    def test_card_3_gem_cost(self):
        card_1 = card.Card(1, 0, yildor.sapphire)
        card_1.set_cost_diamond(1).set_cost_sapphire(2).set_cost_emerald(3)
        self.assertTrue(card_1.number_of_gem_costs() == 3)

    def test_card_2_gem_cost(self):
        card_1 = card.Card(1, 0, yildor.sapphire)
        card_1.set_cost_diamond(1).set_cost_sapphire(2)
        self.assertTrue(card_1.number_of_gem_costs() == 2)

    def test_card_1_gem_cost(self):
        card_1 = card.Card(1, 0, yildor.sapphire)
        card_1.set_cost_diamond(1)
        self.assertTrue(card_1.number_of_gem_costs() == 1)

if __name__ == '__main__':
    unittest.main()
