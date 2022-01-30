"""
The controller responds to the user input and performs interactions on the data model objects.
The controller receives the input, optionally validates it and then passes the input to the model.
"""

import Login


class Controller():
    def __init__(self, model, view, user_id):
        self.model = model
        self.view = view
        self.__user_id = user_id
        self.controller_dashboard()

    def controller_dashboard(self):
        """Calls the General Editors Dashboard,
        processes the users input and navigates to next page"""
        self.view.general_editors_dashboard()
        user_decision = input()
        if user_decision == "1":
            self.controller_article_suggestions_page()
        elif user_decision == "2":
            self.controller_articles_review_page()
        elif user_decision == "3":
            self.controller_contributors_page()
        elif user_decision == "4":
            print("Logout successful")
            Login.login_page()
        else:
            self.view.print_invalid_input()
            self.controller_dashboard()

    def controller_article_suggestions_page(self):
        """Calls the Article Suggestions page, processes
        the users input and navigates to next page"""
        article_suggestions = self.model.get_all_article_suggestions()
        unreviewed_article_suggestions = self.model.filter_article_suggestions_by_assessment(self.__user_id,
                                                                                             article_suggestions,
                                                                                             "un_assessed")
        self.view.article_suggestions_page(len(unreviewed_article_suggestions))
        user_decision = input()
        if user_decision == "1":
            self.controller_new_article_suggestions_page()
        elif user_decision == "2":
            self.controller_reviewed_article_suggestions_page()
        elif user_decision == "3":
            self.controller_suggest_new_article_page()
        elif user_decision == "4":
            self.controller_dashboard()
        else:
            self.view.print_invalid_input()
            self.controller_article_suggestions_page()

    def controller_new_article_suggestions_page(self):
        """Calls the New/Unreviewed Article Suggestions page,
        processes the users input and navigates to next page"""
        self.view.new_article_suggestions_page()
        article_suggestions = self.model.get_all_article_suggestions()
        unreviewed_article_suggestions = self.model.filter_article_suggestions_by_assessment(self.__user_id,
                                                                                             article_suggestions,
                                                                                             "un_assessed")
        unreviewed_article_suggestions = self.model.format_article_suggestions_info_for_print(
            unreviewed_article_suggestions)
        self.view.print_all_article_suggestions_info(unreviewed_article_suggestions)
        user_input_article_id = input(str("Please type an id to proceed: "))
        requested_article = self.model.get_article_suggestion_by_id(user_input_article_id,
                                                                    unreviewed_article_suggestions)
        if user_input_article_id == "back":
            self.controller_article_suggestions_page()
        elif requested_article is not None:
            self.controller_review_suggested_article_page(requested_article)
        else:
            self.view.print_invalid_input()
            self.controller_new_article_suggestions_page()

    def controller_reviewed_article_suggestions_page(self):
        """Calls the Reviewed Article Suggestions page,
        processes the users input and navigates to next page"""
        self.view.reviewed_article_suggestions_page()
        article_suggestions = self.model.get_all_article_suggestions()
        reviewed_article_suggestions = self.model.filter_article_suggestions_by_assessment(self.__user_id,
                                                                                           article_suggestions,
                                                                                           "assessed")
        reviewed_article_suggestions = self.model.format_article_suggestions_info_for_print(
            reviewed_article_suggestions)
        self.view.print_all_article_suggestions_info(reviewed_article_suggestions)
        user_input_article_id = input(str("Please type an id to proceed: "))
        requested_article = self.model.get_article_suggestion_by_id(user_input_article_id, reviewed_article_suggestions)
        if user_input_article_id == "back":
            self.controller_article_suggestions_page()
        elif requested_article is not None:
            self.controller_review_suggested_article_page(requested_article)
        else:
            self.view.print_invalid_input()
            self.controller_reviewed_article_suggestions_page()

    def controller_review_suggested_article_page(self, article: list):
        """Calls the Review page, processes the users input and navigates to next page
        :param list article: clean article info
        [id, title, outline, wordcount, suggested author full name, suggested assignee  full name,
         suggested_reviewer full name, creator username, comments]
         that the user chose on previous page
         (controller_reviewed_article_suggestions_page/controller_new_article_suggestions_page)"""
        self.view.review_suggested_article_page()
        self.view.print_all_article_suggestions_info([article])
        user_decision = input(str("Please type in a number here: "))
        if user_decision == "1":
            self.model.remove_user_assessment_from_article(self.__user_id, article)
            self.model.assess_article_suggestion(self.__user_id, article, "approve")
            self.controller_article_suggestions_page()
        elif user_decision == "2":
            self.model.remove_user_assessment_from_article(self.__user_id, article)
            self.model.assess_article_suggestion(self.__user_id, article, "reject")
            self.controller_article_suggestions_page()
        elif user_decision == "3":
            self.view.comment_on_article_suggestion_page()
            user_comment = input()
            self.model.comment_on_article_suggestion(self.__user_id, user_comment, article)
            self.controller_reviewed_article_suggestions_page()
        elif user_decision == "4":
            self.controller_new_article_suggestions_page()
        else:
            self.view.print_invalid_input()
            self.controller_review_suggested_article_page(article)

    def controller_suggest_new_article_page(self):
        """Calls the Suggest New Article page,
        processes the users input and navigates to next page"""
        user_article_suggestion_info = self.view.suggest_new_article_page()
        decision = input(str("Are you sure you want to suggest this article? (Y/N)"))
        if decision == "Y":
            user_article_suggestion_info.insert(6, self.__user_id)
            self.model.add_article_suggestion(user_article_suggestion_info)
            self.controller_article_suggestions_page()
        elif decision == "N":
            self.controller_article_suggestions_page()
        else:
            self.view.print_invalid_input()
            self.controller_suggest_new_article_page()

    def controller_articles_review_page(self):
        """Calls the Articles in Review page,
        processes the users input and navigates to next page"""
        articles_in_review = self.model.get_all_articles_in_review()
        self.view.articles_review_page(len(articles_in_review))
        user_decision = input()
        if user_decision == "1":
            self.view.print_all_articles_review_information(
                self.model.format_articles_in_review_info_for_print(articles_in_review))
            self.controller_articles_review_page()
        elif user_decision == "2":
            requested_title = input(str("Please input a title: "))
            filtered_articles = self.model.filter_articles_by_title(requested_title, articles_in_review)
            self.view.print_all_articles_review_information(
                self.model.format_articles_in_review_info_for_print(filtered_articles))
            self.controller_articles_review_page()
        elif user_decision == "3":
            requested_author_last_name = input(str("Please input a person by last name: "))
            filtered_articles = self.model.filter_articles_by_author(requested_author_last_name, articles_in_review)
            self.view.print_all_articles_review_information(
                self.model.format_articles_in_review_info_for_print(filtered_articles))
            self.controller_articles_review_page()
        elif user_decision == "4":
            requested_region = input(str("Please input a region: "))
            filtered_articles = self.model.filter_articles_by_region(requested_region, articles_in_review)
            self.view.print_all_articles_review_information(
                self.model.format_articles_in_review_info_for_print(filtered_articles))
            self.controller_articles_review_page()
        elif user_decision == "5":
            print("Status: open/author_invited/initial_check/review/author_revisions)")
            requested_status = input(str("Please input a status: "))
            filtered_articles = self.model.filter_articles_by_status(requested_status, articles_in_review)
            self.view.print_all_articles_review_information(
                self.model.format_articles_in_review_info_for_print(filtered_articles))
            self.controller_articles_review_page()
        elif user_decision == "6":
            self.controller_dashboard()
        else:
            self.view.print_invalid_input()
            self.controller_articles_review_page()

    def controller_contributors_page(self):
        """Calls the Contributors page,
        processes the users input and navigates to next page"""
        contributors = self.model.get_all_contributors()
        self.view.contributors_page(len(contributors))
        action = input(str("Please type a number to proceed: "))
        if action == "1":
            self.view.print_all_contributors_info(contributors)
            self.controller_contributors_page()
        elif action == "2":
            requested_name = input(str("Please input a last name: "))
            filtered_contributors = self.model.filter_contributors_by_last_name(requested_name, contributors)
            self.view.print_all_contributors_info(self.model.format_contributors_info_for_print(filtered_contributors))
            self.controller_contributors_page()
        elif action == "3":
            requested_role = input(str("Please input a person by role (GE/EO/ME/SE): "))
            filtered_contributors = self.model.filter_contributors_by_role(requested_role, contributors)
            self.view.print_all_contributors_info(self.model.format_contributors_info_for_print(filtered_contributors))
            self.controller_contributors_page()
        elif action == "4":
            requested_institution = input(str("Please input an institution: "))
            filtered_contributors = self.model.filter_contributors_by_institution(requested_institution, contributors)
            self.view.print_all_contributors_info(self.model.format_contributors_info_for_print(filtered_contributors))
            self.controller_contributors_page()
        elif action == "5":
            self.controller_dashboard()
        else:
            self.view.print_invalid_input()
            self.controller_contributors_page()
