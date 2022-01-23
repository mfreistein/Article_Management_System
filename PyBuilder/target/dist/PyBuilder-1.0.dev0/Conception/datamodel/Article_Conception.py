from Conception import datamodel as dm

class Article_Conception:
    def __init__(self, title: dm.Title, outline: dm.Outline, wordcount: dm.Worcount, creator: dm.User):
        self.__title = title
        self.__outline = outline
        self.__wordcount = wordcount
        self.__creator = creator
        self.__dates = dm.Dates()
        self.__assessments = dm.Assesments(creator, True)
        self.__suggested_author = None
        self.__suggested_managing_editor = None
        self.__reviewer = None
        self.__comments = dm.Comments(None)
