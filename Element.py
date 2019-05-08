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

    @property
    def left_child_index(self, parent_index):
        """will get the index of the left child of a
           parent element                        """

        return 2 * parent_index

    

    @property
    def right_child_index(self, parent_index):
        """will get the index of the right child of a
           parent element                         """

        return 2 * parent_index

    @property
    def parent_index(self, current_index):
        """will get the index of the parent of a 
           child element using index of child"""

        return math.floor(current_index / 2)
