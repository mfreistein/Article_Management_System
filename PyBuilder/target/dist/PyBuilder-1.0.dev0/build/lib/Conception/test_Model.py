from unittest import TestCase


class TestModel(TestCase):
    def test_get_all_article_suggestions(self):
        from Conception import Model
        self.assertEqual(Model.Model.format_article_suggestions_info_for_print(
            [(75, 77, 25, "7500", "Max P.", "Jenny A.", "Frank the Tank", 1,
              "2021-12-08 18:09:54", "2021-12-08 18:09:54",'{"approvals": [1,3], "rejections": [7]}','{"comments": [["1", "admin", "please accept my proposal", "Fri Dec  3 11:31:03 2021"]]}'), ]),
            [[75, 77, 25, "7500", "Max P.", "Jenny A.", "Frank the Tank", "ad min", [["1", "admin", "please accept my proposal", "Fri Dec  3 11:31:03 2021"]]]])
        self.assertEqual(Model.Model.format_article_suggestions_info_for_print(
            [("75", "title", "outline", 7500, "suggested_author", "suggested_assignee", "suggested_reviewer", 1,
              "y", "x",'{"approvals": [], "rejections": []}','{"comments": []}'), ]),
            [["75", "title", "outline", 7500, "suggested_author", "suggested_assignee", "suggested_reviewer", "ad min", []]])
        self.assertEqual(Model.Model.format_article_suggestions_info_for_print(
            [(75, "title", "outline", 7500, "suggested_author", "suggested_assignee", "suggested_reviewer", 1,
              "2021-12-08 18:09:54", "2021-12-08 18:09:54", '{"approvals": [], "rejections": []}', '{"comments": []}'), ]),
            [[75, "title", "outline", 7500, "suggested_author", "suggested_assignee", "suggested_reviewer", "ad min", []]])


    def test_get_article_suggestion_by_id(self):
        from Conception import Model
        self.assertEqual(Model.Model.get_article_suggestion_by_id("0", [[0], [7], [76], [12]]), [0])
        self.assertEqual(Model.Model.get_article_suggestion_by_id("1", [[0], [7], [76], [12]]), None)
        self.assertEqual(Model.Model.get_article_suggestion_by_id("drölf", [ [7], [76], ["drölf"], [12]]), ["drölf"])

    def test_filter_articles_by_title(self):
        from Conception import Model
        self.assertEqual(Model.Model.filter_articles_by_title("Jumanji", [[0, "Shaft"], [0, "Jumanji"],[0, "White Men can't Jump"], ]),[[0, "Jumanji"], ])
        self.assertEqual(Model.Model.filter_articles_by_title("1", [[0, "1"], [0, "17"], [7, "1"], ]),[[0, "1"], [7, "1"], ])
        self.assertEqual(Model.Model.filter_articles_by_title(17, [[0, 17], [0, "17"], [7, "1"], ]), [[0, 17], ])

    def test_filter_contributors_by_last_name(self):
        from Conception import Model
        self.assertEqual(Model.Model.filter_contributors_by_last_name("Flintstone", [[0, "1", "Flintstone"], [0, "17", 3], [7, "1", 66],]), [[0, "1", "Flintstone"], ])
        self.assertEqual(Model.Model.filter_contributors_by_last_name(55, [[0, "1", "Flintstone"], [0, "17", 3], [7, "1", 55],]), [[7, "1", 55], ])
        self.assertEqual(Model.Model.filter_contributors_by_last_name(55.0, [[0, "1", "Flintstone"], [0, "17", 3], [7, "1", 55],]), [[7, "1", 55], ])
