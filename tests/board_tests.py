import board
from contextlib import contextmanager
import io
import sys
import unittest


class TestBoardMethods(unittest.TestCase):

    @contextmanager
    def setUp(self):
        self.test_output = io.StringIO()
        self.test_err = io.StringIO()
        self.original_output = sys.stdout
        self.original_err = sys.stderr
        sys.stdout = self.test_output
        sys.stderr = self.test_err

    def tearDown(self):
        sys.stdout = self.original_output
        sys.stderr = self.original_err

    def assertPrintedEquals(self, value):
        if self.test_output == None:
            return False

        return self.test_output.getvalue().strip() == value

    def assertPrintedNotEquals(self, value):
        if self.test_output == None:
            return False

        return self.test_output.getvalue().strip() != value

    def test_board_replaceme(self):
        self.assertTrue(True)

    # example of unit test that can capture the printed output
    def test_board_replaceme2(self):
        b = board.Board()
        b.print_top_line()

        # use assertPrintedEquals(value) to test if your
        # printed value matches your expected `value`
        self.assertPrintedEquals("------")


if __name__ == '__main__':
    unittest.main()
