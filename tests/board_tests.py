import board
import io
import sys
import unittest


class TestBoardMethods(unittest.TestCase):

    # before each test, capture the sys.stdout and sys.stderr
    def setUp(self):
        self.test_out = io.StringIO()
        self.test_err = io.StringIO()
        self.original_output = sys.stdout
        self.original_err = sys.stderr
        sys.stdout = self.test_out
        sys.stderr = self.test_err

    # restore sys.stdout and sys.stderr after each test
    def tearDown(self):
        sys.stdout = self.original_output
        sys.stderr = self.original_err

    # assert that sys.stdout would be equal to expected value
    def assertStdoutEquals(self, value):
        self.assertEqual(self.test_out.getvalue().strip(), value)

    # assert that sys.stdout would not be equal to expected value
    def assertStdoutNotEquals(self, value):
        self.assertNotEqual(self.test_out.getvalue().strip(), value)

    # assert that sys.stderr would be equal to expected value
    def assertStderrEquals(self, value):
        self.assertEqual(self.test_err.getvalue().strip(), value)

    # assert that sys.stderr would not be equal to expected value
    def assertStderrNotEquals(self, value):
        self.assertNotEqual(self.test_err.getvalue().strip(), value)

    #
    # unit tests go here
    #

    # example of unit test that can capture the printed output
    def test_board_replaceme(self):
        b = board.Board()
        b.print_top_line()

        # use assertStdoutEquals(value) to test if your
        # printed value matches your expected `value`
        self.assertStdoutEquals("------")


if __name__ == '__main__':
    unittest.main()
