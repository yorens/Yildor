import unittest
import bank
import yildor


class TestBankMethods(unittest.TestCase):

    def test_replaceme(self):
        self.assertTrue(True)

    def test_take_away_one_chip_from_bank(self):
        b = bank.Bank(7, 7, 8, 7, 7)
        b.withdraw_one_coin(yildor.emerald)
        self.assertTrue(b.balance(yildor.emerald) == 7)

    def test_withdraw_too_much(self):
        b = bank.Bank(7, 7, 8, 7, 7)
        b.withdraw_one_coin(yildor.emerald)
        b.withdraw_one_coin(yildor.emerald)
        b.withdraw_one_coin(yildor.emerald)
        b.withdraw_one_coin(yildor.emerald)
        b.withdraw_one_coin(yildor.emerald)
        b.withdraw_one_coin(yildor.emerald)
        b.withdraw_one_coin(yildor.emerald)
        b.withdraw_one_coin(yildor.emerald)
        b.withdraw_one_coin(yildor.emerald)
        b.withdraw_one_coin(yildor.emerald)
        b.withdraw_one_coin(yildor.emerald)
        b.withdraw_one_coin(yildor.emerald)
        b.withdraw_one_coin(yildor.emerald)
        self.assertTrue(b.balance(yildor.emerald) == 0)

    def test_deposit_too_many_coins(self):
        b = bank.Bank(7, 7, 7, 7, 7)
        b.add_chip_to_bank(yildor.diamond)
        b.add_chip_to_bank(yildor.diamond)
        self.assertTrue(b.balance(yildor.diamond) == 7)

if __name__ == '__main__':
    unittest.main()
