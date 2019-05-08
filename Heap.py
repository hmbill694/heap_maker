from Element import Element
import math


class Heap(object):
    """The heap class is where all the algorithm functions will go
        this includes building the heap, organizing the heap and 
        manipulating the heap.                                 """

    def __init__(self):
        """Constructor"""

        self.__max_capacity = 0
        self.__capacity = 0
        self.__element_list = list()

    @property
    def max_capacity(self):
        """Returns max_capacity property"""

        return self.__max_capacity

    @max_capacity.setter
    def max_capacity(self, in_max_capacity):
        """Setter for max_capacity property"""

        self.__max_capacity = in_max_capacity

    @property
    def current_capacity(self):
        """Returns capacity property"""

        return self.__capacity

    @current_capacity.setter
    def current_capacity(self, in_capacity):
        """Setter for capacity property"""

        self.__capacity = in_capacity

    @property
    def element_list(self):
        """Getter for list"""

        return self.__element_list

    @element_list.setter
    def element_list(self, new_list):
        """Setter for list"""
        self.__element_list = new_list

    def heapify(self,index):
        """"""

        if index > self.element_list.le
        parent_element = self.element_list[index]
        
        # get index of left and right child elements
        left_element_index = parent_element.left_element_index
        right_element_index = parent_element.right_element_index
       
        # get elements from list of elements in the heap
        left_element = self.element_list[left_element_index]
        right_element = self.element_list[right_element_index]

        






    @staticmethod
    def initialize_heap(self,in_capacity, in_data):
        """This static method will return a created heap
           with a capacity of varaible max_capacity that is
           populated by elements all with the value of
           None                                    """

        # create heap and give it a max_capacity and a current capacity
        my_heap = Heap()
        my_heap.current_capacity = in_capacity
        my_heap.max_capacity = len(in_data)
        
        for entry in in_data:
            element = Element(None)
            element.value = entry
            my_heap.element_list.append(element)
            my_heap.max_capacity += 1

        return my_heap

    @staticmethod
    def swap_elements(self, element1, element2):
        element1 , element2 = element2, element1
    # def build_heap(self, in_data):
    #     """This function will build the heap from a inputed
    #        list of integers. It will also set the max_capacity and
    #        heapify the array                           """

    #     self.max_capacity = len(in_data)

    #     count = 0
    #     while count < self.max_capacity:
    #         self.element_list[count].value = in_data[count] 
    #         print(self.element_list[count].value)
    #         count += 1
        
    #     [print(element.value) for element in self.element_list]

    #     for entry,element in zip(in_data,self.element_list):
    #         element.value

    #     [print(element.value) for element in self.element_list]

    #     print("end")
        

        
