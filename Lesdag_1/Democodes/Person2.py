class Person:

    residence = "Harderwijk"

    __slots__ = ("__name", "__residence")

    def __init__(self, name, residence):
        self.__name = name
        self.__residence = residence

    def tell(self):
        return "I am {}  and I live in {}.".format(self.__name, self.__residence)

    def move(self, new_residence):
        self.__residence = new_residence

    def __str__(self):
        return "name: " + self.__name + " - " + "residence: " + self.__residence