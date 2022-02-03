from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import View

class TestView(TestCase):
    def test_View_invalid_input(self):
        expected_output = "This is not a valid input. Please try again\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            View.View.print_invalid_input()
            self.assertEqual(fake_out.getvalue(), expected_output)
    def test_View_new_article_suggestions_page(self):
        expected_output = "\nNew Article Suggestions\n\nIf you would like to review an articles, please type in the article id.\nOr type 'back' to return to the previous page\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            View.View.new_article_suggestions_page()
            self.assertEqual(fake_out.getvalue(), expected_output)
