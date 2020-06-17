import unittest
import chip
import yildor

class TestChipMethods(unittest.TestCase):

    def test_chip_create_diamond(self):
        self.assertTrue(chip.create_diamond().chip_type == yildor.diamond)

    def test_chip_create_sapphire(self):
        self.assertTrue(chip.create_sapphire().chip_type == yildor.sapphire)

    def test_chip_create_emerald(self):
        self.assertTrue(chip.create_emerald().chip_type == yildor.emerald)

    def test_chip_create_ruby(self):
        self.assertTrue(chip.create_ruby().chip_type == yildor.ruby)

    def test_chip_create_onyx(self):
        self.assertTrue(chip.create_onyx().chip_type == yildor.onyx)

if __name__ == '__main__':
    unittest.main()
