import unittest


class TestGameMethods(unittest.TestCase):

    def setup(self):
        # example of creating an internal
        # game object in case we need to maintain
        # state in between tests
        # self.game = Game()
        return

    def tearDown(self):
        # clear self.game if necessary
        return

    def test_replaceme(self):
        self.assertTrue(True)

    # def test_broken(self):
    #     self.assertTrue(False)

    def test_isEqual(self):
        self.assertEqual("a", "a")


if __name__ == '__main__':
    unittest.main()
