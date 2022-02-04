class Article_Conception():
    __title = ""
    __outline = ""
    __wordcount = ""
    __suggested_author = ""
    __suggested_assignee = ""
    __suggested_reviewer = ""
    __creator = ""
    __date_created = ""
    __date_last_updated = ""
    __assessments = ""
    __comments = ""

    def __str__(self):
        type = ["title: ", "outline: ", "wordcount: ", "suggested_author: ", "suggested_assignee: ",
                "suggested_reviewer: ", "creator: ", "date_created: ", "date_last_updated: ",
                "assessments: ", "comments: "]
        info = [self.__title, self.__outline, self.__wordcount, self.__suggested_author, self.__suggested_assignee,
                self.__suggested_reviewer, self.__creator, self.__date_created, self.__date_last_updated,
                self.__assessments, self.__comments]
        count = 0
        final_print = []
        for x in info:
            if x != "":
                final_print.append(type[count] + str(x))
            count += 1
        return str(final_print)

    def setTitle(self, title):
        self.__title = title
        return self

    def setOutline(self, outline):
        self.__outline = outline
        return self

    def setWordcount(self, wordcount):
        self.__wordcount = wordcount
        return self

    def setSuggested_author(self, suggested_author):
        self.__suggested_author = suggested_author
        return self

    def setSuggested_assignee(self, suggested_assignee):
        self.__suggested_assignee = suggested_assignee
        return self

    def setSuggested_reviewer(self, suggested_reviewer):
        self.__suggested_reviewer = suggested_reviewer
        return self

    def setCreator(self, creator):
        self.__creator = creator
        return self

    def setDate_created(self, date_created):
        self.__date_created = date_created
        return self

    def setDate_last_updated(self, date_last_updated):
        self.__date_last_updated = date_last_updated
        return self

    def setAssessments(self, assessments):
        self.__assessments = assessments
        return self

    def setComments(self, comments):
        self.__comments = comments
        return self
