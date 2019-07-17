import math


class Element(object):
    def __init__(self, in_value):
        """Constructor"""

        self.__value = in_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        """Setter for internal value"""

        self.__value = new_value
