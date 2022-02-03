"""
GUI replacement
"""
# from src.Conception.datamodel import Datamodel_Article_Conception
# import Datamodel_Article_Conception
from src.Conception import Datamodel_Article_Conception

class View:
    """
    All output to user is generated here
    """
    @staticmethod
    def general_editors_dashboard():
        """
        Console Output Dashboard for General Editors
        User given choice between:
        1 View Article Suggestions
        2 View Articles
        3 View Contributors
        4 Logout
        """
        print("")
        print("Welcome to the General Editor's Dashboard")
        print("")
        print("1 View Article Suggestions")
        print("2 View Articles")
        print("3 View Contributors")
        print("4 Logout")
        print("")
        print("Please type a number to proceed:")

    @staticmethod
    def article_suggestions_page(num_unreviewed_article_suggestions: int):
        """
        Console Output Article Suggestions page
        User given choice between:
        1 View new article suggestions
        2 View reviewed article suggestions
        3 Suggest a new Article
        4 Return to General Editor Dashboard
        :param int num_unreviewed_article_suggestions:
        """
        print("")
        print("Welcome to the article suggestions page")
        print("")
        print(str(num_unreviewed_article_suggestions) + " new article suggestions for you to assess")
        print("")
        print("1 View new article suggestions")
        print("2 View reviewed article suggestions")
        print("3 Suggest a new Article")
        print("4 Return to General Editor Dashboard")
        print("")
        print("Please type a number to proceed: ")

    @staticmethod
    def print_invalid_input():
        """
        Prints invalid input error message
        """
        print("This is not a valid input. Please try again")

    @staticmethod
    def new_article_suggestions_page():
        """
        Console Output Unreviewed/New Article Suggestions page
        User instructed to type in article id of choice or "back"
        for previous page "Console Output Article Suggestions" /
        article_suggestions_page
        """
        print("")
        print("New Article Suggestions")
        print("")
        print("If you would like to review an articles, please type in the article id.")
        print("Or type 'back' to return to the previous page")

    @staticmethod
    def reviewed_article_suggestions_page():
        """
        Console Output Reviewed Article Suggestions
        User instructed to type in article id of choice or "back"
        for previous page "Console Output Article Suggestions" /
        article_suggestions_page
        """
        print("")
        print("Reviewed Article Suggestions")
        print("")
        print("If you would like change your review or comment on an article,"
              " please type in the article id.")
        print("Or type 'back' to return to the previous page")

    @staticmethod
    def review_suggested_article_page():
        """
        Console Output for Editing Suggested Article
        User given choice between:
        1 approve
        2 reject
        3 comment
        4 return to previous page
        (Console Output Reviewed Article Suggestions/reviewed_article_suggestions_page)
        """
        print("")
        print("Suggested Article")
        print("")
        print("1 approve")
        print("2 reject")
        print("3 comment")
        print("4 return to previous page")
        print("")
        print("What would you like to do?")

    @staticmethod
    def comment_on_article_suggestion_page():
        """
        Console Output for Commenting on Article page
        User instructed to type in comment
        """
        print("Please comment here: ")

    @staticmethod
    def print_all_article_suggestions_info(article_suggestions: list):
        """
        Prints important Article Suggestions Information
        :param list article_suggestions: [[id, title, outline, wordcount, suggested_author,
        suggested assignee, suggested_reviewer, creator, comments],]
        """
        for article in article_suggestions:
            print("")
            print("id: " + str(article[0]))
            print("Title: " + article[1])
            print("Outline: " + article[2])
            print("Wordcount: " + str(article[3]))
            print("Suggested Author: " + article[4])
            print("Suggested Assignee: " + article[5])
            print("Suggested Reviewer: " + article[6])
            print("Creator: " + article[7])
            print("Comments: ")
            for comment_info in article[8]:
                print(comment_info[1] + " commented on " + comment_info[3][:comment_info[3].index(" ")] + ":")
                print(comment_info[2])
            print("")

    @staticmethod
    def suggest_new_article_page() -> list:
        """
        Console Output for Suggesting New Article page
        Instructs the user to input relevant information
        returns a list of the input information with given indexes in parentheses
        mandatory: (0) title, (1) outline, (2) wordcount
        optional: (3) author, (4) assignee, (5) reviewer, (7) comments
        """
        print("")
        print("Suggest a new article")
        print("")
        title = input(str("Please add a title: "))
        outline = input(str("Please add an article outline: "))
        wordcount = input(str("Please add a max. word count: "))
        author = input(str("Feel free to suggest an author: "))
        assignee = input(str("Feel free to suggest an assignee: "))
        reviewer = input(str("Feel free to suggest a reviewer: "))
        comments = input(str("Feel free to comment: "))
        article = Datamodel_Article_Conception.Article_Conception().setTitle(title).\
            setOutline(outline).\
            setWordcount(wordcount).\
            setSuggested_author(author).\
            setSuggested_assignee(assignee).\
            setSuggested_reviewer(reviewer).\
            setComments(comments)
        print(article)
        return [title, outline, wordcount, author, assignee, reviewer, comments]

    @staticmethod
    def articles_review_page(num_articles_in_review: int):
        """
        Console Output for Articles in Review page
        User given choice between:
        1 View all articles in review
        2 Filter for articles by title
        3 Filter for articles by person
        4 Filter for articles by region
        5 Filter for articles by status
        6 Return to General Editor Dashboard
        """
        print("Welcome to the articles page")
        print("")
        print("There are " + str(num_articles_in_review) + " articles currently in review")
        print("")
        print("1 View all articles in review")
        print("2 Filter for articles by title")
        print("3 Filter for articles by author")
        print("4 Filter for articles by region")
        print("5 Filter for articles by status")
        print("6 Return to General Editor Dashboard")
        print("")
        print("Please type a number to proceed:  ")

    @staticmethod
    def print_all_articles_review_information(articles_in_review: list):
        """
        Prints important Articles in Review Information
        :param articles_in_review:
        [[id, title, assignee, author, first_reviewer, last updated, type,
        edition, status, outline, wordcount, region, theme],]
        """
        for article in articles_in_review:
            print("id: " + str(article[0]))
            print("title: " + article[1])
            print("assignee: " + str(article[2]))
            print("author: " + str(article[3]))
            print("first_reviewer: " + str(article[4]))
            print("last updated: " + str(article[5]))
            print("type: " + article[6])
            print("edition: " + str(article[7]))
            print("status: " + article[8])
            print("outline: " + article[9])
            print("wordcount: " + str(article[10]))
            print("region: " + article[11])
            print("theme: " + article[12])

    @staticmethod
    def contributors_page(num_contributors: int):
        """
        Console Output Contributors
        User given choice between:
        1 View all contributors
        2 Filter for contributors by last name
        3 Filter for articles by role
        4 Filter for articles by institution
        5 Return to General Editor Dashboard
        """
        print("Welcome to the Contributors page")
        print("")
        print("There are " + str(num_contributors) + " active contributors")
        print("")
        print("1 View all contributors")
        print("2 Filter for contributors by last name")
        print("3 Filter for articles by role")
        print("4 Filter for articles by institution")
        print("5 Return to General Editor Dashboard")
        print("")

    @staticmethod
    def print_all_contributors_info(contributors_info: list):
        """
        Prints important Contributors Information
        Name, Email, Institution, Role
        :param list contributors_info: [[id, full name, email, institution, role],]
        """
        for contributor_info in contributors_info:
            print("")
            print("Name: " + contributor_info[1])
            print("Email: " + contributor_info[2])
            print("Institution: " + contributor_info[3])
            print("Role: " + contributor_info[4])
            print("")
