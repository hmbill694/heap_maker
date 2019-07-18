from model.Heap import Heap
from model.Util import Util
import sys


def main():
    input_data = list()

    print("Hello, welcome to the heap maker," +
          "will you be using a file or inputing manually: ")
    while True:
        choice = input("1. - File, 2.- Manual Input, 3: - Exit: ")
        if choice == "1":
            input_data = Util().file_input()
            break
        elif choice == "2":
            input_data = Util().manual_input()
            break
        elif choice == "3":
            print("Have a nice day")
            sys.exit()
        else:
            print("Please enter an integer of value 1, 2, or 3")

    print("The inputed list is:\n")
    print(input_data)

    my_heap = Heap().initialize_heap(len(input_data), input_data)

    while True:
        print("\n")
        print("What operations would you like to preform on the heap")
        print("1. Insert into heap")
        print("2. Delete value from the heap")
        print("3. Extract max")
        print("4. Use Heapsort (will only display sorted heap)")
        print("5. Print the heap")
        print("6. Exit program")

        choice = input("Preform operation: ")

        if choice == "1":
            value = int(input("What value would you like to insert: "))
            my_heap.insert(value)
        elif choice == "2":
            delete = int(
                input(
                    "What please enter the element number you want to delete in range 0 - {}: "
                    .format(my_heap.current_capacity - 1)))
            while True:
                if delete > my_heap.current_capacity:
                    print("Please enter a element within the range {}".format(
                        my_heap.current_capacity - 1))
                else:
                    break
            my_heap.delete(delete)
        elif choice == "3":
            element = my_heap.extract_root()
            print("The value extracted from the heap is: {}".format(
                element.value))
        elif choice == "4":
            my_heap.heap_sort()
        elif choice == "5":
            my_heap.print_heap()
        elif choice == "6":
            sys.exit()
        else:
            print("Please enter a valid input")


if __name__ == "__main__":
    main()
