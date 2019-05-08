import sys


class Util(object):
    """The Util is implemented to allow main to be more readable"""

    def __init__(self):
        pass

    @staticmethod
    def manual_input(input_data):
        """A method that handles if the user chooses to manually
           enter the working data                            """

        print("Enter in the integers you would like to use.")
        print("Input \"d\" when done")

        while True:

            value = input()
            try:
                if value == "d" or value == "D":
                    break

                value = int(value)
                input_data.append(value)

            except ValueError:
                print("Enter only integers or \"d\" to finish")

        

    @staticmethod
    def file_input(input_data):
        """A method that handles if the user chooses to use a file
           to handle inputing the file                         """

        file_name = input("Please enter file name:  ")
        validate = input(file_name + " --Correct?" + " Y (Yes) " +
                         " N (No):  ")
        validate = validate.lower()

        if validate == "y":
            try:
                with open(file_name, "r") as input_file:
                    for line in input_file:
                        line = line.strip()
                        input_data.append(line)
            except Exception:
                sys.exit()

        else:
            print("Re-enter file name:  ")
