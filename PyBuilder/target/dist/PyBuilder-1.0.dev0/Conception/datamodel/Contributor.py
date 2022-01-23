from abc import ABCMeta, abstractclassmethod

class IContributor(metaclass=ABCMeta, name: str, email: str, institution: str):

    @abstractclassmethod
    def get_name():
        """gets contributors name"""

class Author(IContributor):
    def __init__(self):
        self.__name = name
        self.__email =
        self.__institution =


class Managing_Editor(IContributor):
    def __init__(self):
        self.__name =
        self.__email =
        self.__institution =


class Reviewer(IContributor):
    def __init__(self):
        self.__name =
        self.__email =
        self.__institution =

class ContributorFactory:
    @staticmethod
    def build_contributor(name: str, email: str, institution: str, contributor_role):
        if contributor_role = "author":
            return Author()
        if contributor_role = "managing editor":
            return Managing_Editor()
        if contributor_role = "reviewer":
            return Reviewer()
        print("Invalid Role")
        return -1
        #raise exception