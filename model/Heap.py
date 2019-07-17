from model.Element import Element
import math
import sys
import pprint


class Heap(object):
    """The heap class is where all the algorithm functions will go
        this includes building the heap, organizing the heap and 
        manipulating the heap.                                 """

    def __init__(self):
        """Constructor"""
        self.__capacity = 0
        self.__element_list = list()

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

    def heapify(self, index):
        """A method that will reorder the heap by comparing parent element 
           values to child element values. If the value of the child elements
           violate the heap property then they will be swapped to preserve it"""
        largest = None
        min_int = -sys.maxsize
        left_index = (2 * index) + 1
        right_index = (2 * index) + 2
        parent = self.element_list[index]

        # Try and grab elements from the list, if there is an error
        # create dummy elements to use in calculations
        if (left_index + 1) <= self.current_capacity:
            left = self.element_list[left_index]
        else:
            left = Element(min_int)
            right = Element(min_int)

        if (right_index + 1) <= self.current_capacity:
            right = self.element_list[right_index]
        else:
            right = Element(min_int)

        if left_index <= (self.current_capacity -
                          1) and left.value > parent.value:
            largest = left
        else:
            largest = parent

        if right_index <= (self.current_capacity -
                           1) and right.value >= largest.value:
            largest = right

        largest_index = None

        if largest == left:
            largest_index = left_index
        else:
            largest_index = right_index

        if largest != parent:
            Heap().swap_elements(self.element_list, index, largest_index)
            self.heapify(largest_index)

    @staticmethod
    def initialize_heap(in_capacity, in_data):
        """This static method will return a created heap
           with a capacity of varaible max_capacity that is
           populated by elements all with the value of
           None                                    """

        # create heap and give it  a current capacity
        my_heap = Heap()
        my_heap.current_capacity = in_capacity

        for entry in in_data:
            element = Element(None)
            element.value = entry
            my_heap.element_list.append(element)

        for element in range((math.floor(len(my_heap.element_list) / 2) - 1),
                             -1, -1):
            my_heap.heapify(element)

        return my_heap

    @staticmethod
    def swap_elements(element_list, element_1_index, element_2_index):
        """Swaps values"""
        element_list[element_1_index], element_list[
            element_2_index] = element_list[element_2_index], element_list[
                element_1_index]

    def print_heap(self):
        """Prints the heap"""
        value_list = [a.value for a in self.element_list]
        print(value_list)

    def heap_sort(self):
        """Place elements in order of ascending value. This method will then 
           print the sorted list before reheapifying the heap elements"""
        saved_size = self.current_capacity
        current_element = self.current_capacity - 1

        # swap first and last element in heap and reheapify the 1st element
        # do this while the size of the heap is greater than 1
        while self.current_capacity > 1:
            Heap.swap_elements(self.element_list, 0, current_element)
            self.current_capacity -= 1
            current_element -= 1
            self.heapify(0)

        # print heap after sort
        self.print_heap()

        # reset capacity
        self.current_capacity = saved_size

        # reheapify elements in heap
        for element in range((math.floor(len(self.element_list) / 2) - 1), -1,
                             -1):
            self.heapify(element)

    def extract_root(self):
        """Removes the root element by swapping with the last element
           and then popping it off"""

        root_element = None

        # swap root and last value in heap
        Heap.swap_elements(self.element_list, 0, self.current_capacity - 1)

        # pop of last element and set new capacity
        root_element = self.element_list.pop(self.current_capacity - 1)
        self.current_capacity = len(self.element_list)

        # reheapify
        self.heapify(0)

        return root_element

    def insert(self, value):
        new_element = Element()
        new_element.value = value
