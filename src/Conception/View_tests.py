from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import View

class TestView(TestCase):

    def test_general_editors_dashboard(self):
        expected_output = "\nWelcome to the General Editor's Dashboard\n\n1 View Article Suggestions\n2 View Articles\n3 View Contributors\n4 Logout\n\nPlease type a number to proceed:\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            View.View.general_editors_dashboard()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_article_suggestions_page(self):
        expected_output = "\nWelcome to the article suggestions page\n\n3 new article suggestions for you to assess\n\n1 View new article suggestions\n2 View reviewed article suggestions\n3 Suggest a new Article\n4 Return to General Editor Dashboard\n\nPlease type a number to proceed: \n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            View.View.article_suggestions_page(3)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_print_invalid_input(self):
        expected_output = "This is not a valid input. Please try again\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            View.View.print_invalid_input()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_new_article_suggestions_page(self):
        expected_output = "\nNew Article Suggestions\n\nIf you would like to review an articles, please type in the article id.\nOr type 'back' to return to the previous page\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            View.View.new_article_suggestions_page()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_reviewed_article_suggestions_page(self):
        expected_output = "\nReviewed Article Suggestions\n\nIf you would like change your review or comment on an article, please type in the article id.\nOr type 'back' to return to the previous page\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            View.View.reviewed_article_suggestions_page()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_review_suggested_article_page(self):
        expected_output = "\nSuggested Article\n\n1 approve\n2 reject\n3 comment\n4 return to previous page\n\nWhat would you like to do?\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            View.View.review_suggested_article_page()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_comment_on_article_suggestion_page(self):
        expected_output = "Please comment here: \n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            View.View.comment_on_article_suggestion_page()
            self.assertEqual(fake_out.getvalue(), expected_output)



