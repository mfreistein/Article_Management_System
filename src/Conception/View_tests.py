from unittest import TestCase


class TestView(TestCase):
    def print_invalid_input(self):
        from View import View
        self.assert_stdout("This is not a valid input. Please try again")
