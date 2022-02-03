"""
The model is responsible for managing the data of the application.
It receives user input from the controller.
"""

import json
import datetime
# from Databases import Article_Info_Conception as aic_db
# from Databases import Contributor_Info_Review as cir_db
# from Databases import Article_Info_Review as air_db
# from Databases import Users as users
from src.Databases import Article_Info_Conception as aic_db
from src.Databases import Contributor_Info_Review as cir_db
from src.Databases import Article_Info_Review as air_db
from src.Databases import Users as users
from src.Conception import Exceptions

class Model:

    @staticmethod
    def get_all_article_suggestions() -> list:
        """
        Gets full list of suggested articles from Database "Article_Info_Conception" and returns it
        :returns: [(id, title, outline, wordcount, suggested_author, suggested_assignee,
        suggested_reviewer, creator, date_created, date_last_updated, assessments, comments)]
        """
        return aic_db.get_all_article_suggestions()

    @staticmethod
    def get_article_suggestion_by_id(article_id: str, article_suggestions: list) -> list:
        """returns the article with the matching id from article suggestions list"""
        for article in article_suggestions:
            if article_id == str(article[0]):
                return article
        return None

    @staticmethod
    def format_article_suggestions_info_for_print(article_suggestions_info_raw: list) -> list:
        """
        Reformats the full article suggestion information to relevant information
        for Console Output print out
        :param article_suggestions_info_raw:
        full article suggestions information from sql database
        [(id, title, outline, wordcount, suggested_author, suggested_assignee, suggested_reviewer,
        creator_id, date_created, date_last_updated, assessments, comments])
        :return list: [[id, title, outline, wordcount, suggested_author, suggested assignee,
        suggested_reviewer, creator_full_name, comments],]
        """
        article_suggestions_info_clean = []
        for article_suggestion_info_raw in article_suggestions_info_raw:
            article_suggestion_info_clean = []
            for info in range(0, 7):
                article_suggestion_info_clean.append(article_suggestion_info_raw[info])
            creator_info = users.get_user_info_from_id(article_suggestion_info_raw[7])[0]
            creator_full_name = str(creator_info[1]) + " " + str(creator_info[2])
            article_suggestion_info_clean.append(creator_full_name)
            comments = article_suggestion_info_raw[11]
            comments = json.loads(comments)
            article_suggestion_info_clean.append(comments['comments'])
            article_suggestions_info_clean.append(article_suggestion_info_clean)
        return article_suggestions_info_clean

    @staticmethod
    def filter_article_suggestions_by_assessment(user_id: int, article_suggestions: list, assessment: str) -> list:
        """
        Takes a user_id, a list of article suggestions and a type of assessment and filters out the
        "assessed" or "un_assessed" articles depending on the parameter "assessment"
        :param assessment:
        :param article_suggestions:
        :param user_id:
        :param int user_id, list article_suggestions,
        str assessment: assessment is either "assessed" or "un_assessed"
        :return list filtered_article_suggestions_list:
        """
        try:
            if assessment != "assessed" and assessment != "un_assessed":
                raise Exceptions.GeneralException("Error: Must specify if article has been assessed or not!")
        except Exceptions.GeneralException as e:
            print(e.message)
        if assessment == "un_assessed":
            return [article_suggestion for article_suggestion in article_suggestions
                    if str(user_id) not in json.loads(article_suggestion[10])['approvals'] and str(user_id) not in json.loads(article_suggestion[10])['rejections']]
        if assessment == "assessed":
            return [article_suggestion for article_suggestion in article_suggestions
                    if str(user_id) in json.loads(article_suggestion[10])['approvals'] or str(user_id) in json.loads(article_suggestion[10])['rejections']]
        return None

    @staticmethod
    def assess_article_suggestion(user_id: int, article: list, assessment: str):
        """
        takes user_id, article and "approve" or "reject" string.
        adds user_id to assessments list "approvals" or "rejections"
        sends assessments to Database "Article_Info_Conception"
        :param int user_id, list article, str assessment:
        """
        try:
            if assessment != "approve" and assessment != "reject":
                raise Exceptions.GeneralException("Error: Must specify if article has been approved or rejected!")
        except Exceptions.GeneralException as e:
            print(e.message)
        assessments = aic_db.get_article_assessments(article[0])
        assessments = json.loads(assessments[0][0])
        if assessment == "approve":
            assessments['approvals'].append(str(user_id))
        elif assessment == "reject":
            assessments['rejections'].append(str(user_id))
        assessments = json.dumps(assessments)
        aic_db.set_article_assessments(assessments, article[0])

    @staticmethod
    def remove_user_assessment_from_article(user_id: int, article: list):
        """
        takes user_id and article.
        removes user_id from assessments list "rejections" and "approvals"
        and sends assessments to Database "Article_Info_Conception"
        :param int user_id, list article:
        """
        assessments = aic_db.get_article_assessments(article[0])
        assessments = json.loads(assessments[0][0])
        if str(user_id) in assessments['rejections']:
            cleaned_list = [value for value in assessments['rejections'] if value != str(user_id)]
            assessments['rejections'] = cleaned_list
        if str(user_id) in assessments['approvals']:
            cleaned_list = [value for value in assessments['approvals'] if value != str(user_id)]
            assessments['approvals'] = cleaned_list
        assessments = json.dumps(assessments)
        aic_db.set_article_assessments(assessments, article[0])

    @staticmethod
    def comment_on_article_suggestion(user_id: int, user_comment: str, article: list):
        """
        takes user_id, user_comment and article. Formats comment and sends comment
        to Database "Article_Info_Conception"
        :param int user_id, str user_comment, list article:
        """
        username = users.get_user_info_from_id(user_id)[0][3]
        comments = aic_db.get_article_suggestion_comments(article[0])
        comments = json.loads(comments[0][0])
        date_now = datetime.datetime.now()
        date_now = date_now.strftime("%Y-%m-%d %H:%M:%S")
        addition = [str(user_id), username, user_comment, date_now]
        comments['comments'].append(addition)
        comments = json.dumps(comments)
        aic_db.add_article_suggestion_comment(comments, article[0])

    @staticmethod
    def add_article_suggestion(article_suggestion_info: list):
        """
        Gets new article suggestion info, formats comments for Database,
        adds dates created and last updated
        and sends it to Database "Article_Info_Conception" in tuple:
        (id, title, outline, wordcount, suggested_author, suggested_assignee, suggested_reviewer,
        creator, date_created, date_last_updated, assessments, comments)
        """
        assessments = json.dumps({"approvals": [article_suggestion_info[6]], "rejections": []})
        if article_suggestion_info[7] is None:
            comments = json.dumps({"comments": []})
        else:
            date_now = datetime.datetime.now()
            user_info = users.get_user_info_from_id(article_suggestion_info[6])
            comment_form = [article_suggestion_info[6], user_info[0][3],
                            article_suggestion_info[7], date_now.strftime("%Y-%m-%d %H:%M:%S")]
            comments = json.dumps({"comments": [comment_form]})
        tuple_vals = (article_suggestion_info[0], article_suggestion_info[1],
                int(article_suggestion_info[2]), article_suggestion_info[3],
                article_suggestion_info[4], article_suggestion_info[5],
                article_suggestion_info[6], date_now.strftime("%Y-%m-%d %H:%M:%S"),
                date_now.now().strftime("%Y-%m-%d %H:%M:%S"), assessments, comments)
        aic_db.add_article_suggestion(tuple_vals)

    @staticmethod
    def get_all_articles_in_review() -> list:
        """
        Gets full list of articles in review from Database "Article_Info_Review" and returns it
        :return list:
        [(id, title, assignee_id, author_id, first_reviewer_id, second_reviewer_id,
        date_created, date_last_updated, due_date, type, edition, status,
        outline, wordcount, region, theme])
        """
        return air_db.get_all_articles_in_review()

    @staticmethod
    def format_articles_in_review_info_for_print(articles_in_review_info_raw: list) -> list:
        """
        Reformats the full article in review information
        to relevant information for Console Output print out
        :param list articles_in_review_info_raw:
        full article in review information from sql database
        :return list: [[id, title, assignee, author, first_reviewer, last updated, type, edition,
        status, outline, wordcount, region, theme],]
        """
        articles_in_review_info_clean = []
        for article_in_review_info_raw in articles_in_review_info_raw:
            article_in_review_info_clean = []
            assignee_info = cir_db.get_contributor_info_from_id(article_in_review_info_raw[2])[0]
            article_in_review_info_clean.append(str(assignee_info[1]) + " " + str(assignee_info[2]))
            author_info = cir_db.get_contributor_info_from_id(article_in_review_info_raw[3])[0]
            article_in_review_info_clean.append(str(author_info[1]) + " " + str(author_info[2]))
            first_reviewer_info = cir_db.get_contributor_info_from_id(article_in_review_info_raw[4])[0]
            article_in_review_info_clean.append(str(first_reviewer_info[1]) + " " + str(first_reviewer_info[2]))
            for info in [0, 1, 6, 9, 10, 11, 12, 13, 14, 15]:
                article_in_review_info_clean.append(article_in_review_info_raw[info])
            articles_in_review_info_clean.append(article_in_review_info_clean)
        return articles_in_review_info_clean

    @staticmethod
    def filter_articles_by_title(requested_title: str, articles: list) -> list:
        """filters for requested title from a list of articles"""
        return [article for article in articles if requested_title == article[1]]

    @staticmethod
    def filter_articles_by_author(requested_author_last_name: str, articles: list) -> list:
        """
        gets author's id from last name and filters for requested title from a list of articles
        :return list article:
        """
        author_ids = cir_db.get_id_from_last_name(requested_author_last_name)
        author_ids = [author_id[0] for author_id in author_ids]
        return [article for article in articles if article[3] in author_ids]

    @staticmethod
    def filter_articles_by_region(requested_region: str, articles: list) -> list:
        """filters for requested region from a list of articles"""
        return [article for article in articles if requested_region == article[14]]

    @staticmethod
    def filter_articles_by_status(requested_status: str, articles: list) -> list:
        """filters for requested status from a list of articles"""
        return [article for article in articles if requested_status == article[11]]

    @staticmethod
    def get_all_contributors() -> list:
        """
        Gets full list of contributors from Database "Contributor_Info_Review" and returns it
        :return list: [(id, first_name, last_name, email, institution, role,])
        """
        return cir_db.get_all_contributors()

    @staticmethod
    def format_contributors_info_for_print(contributors_info_raw) -> list:
        """
        Combines first and last name in contributors information list
        :param list articles_in_review_info_raw:
        [(id, first_name, last_name, email, institution, role])
        :return list: [id, full_name, email, institution, role]
        """
        contributors_info_clean = []
        for contributor_info_raw in contributors_info_raw:
            contributor_info_clean = [str(contributor_info_raw[1]) + " " + str(contributor_info_raw[2])]
            for info in [0, 3, 4, 5]:
                contributor_info_clean.append(contributor_info_raw[info])
            contributors_info_clean.append(contributor_info_clean)
        return contributors_info_clean

    @staticmethod
    def filter_contributors_by_last_name(requested_name: str, contributors: list) -> list:
        """filters for last name from a list of contributors"""
        return [contributor for contributor in contributors if contributor[2] == requested_name]

    @staticmethod
    def filter_contributors_by_role(requested_role: str, contributors: list) -> list:
        """filters for role from a list of contributors"""
        return [contributor for contributor in contributors if requested_role == contributor[5]]

    @staticmethod
    def filter_contributors_by_institution(requested_institution: str, contributors: list) -> list:
        """filters for institution from a list of contributors"""
        return [contributor for contributor in contributors if requested_institution == contributor[4]]
