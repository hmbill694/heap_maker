import sys


class Util(object):
    """The Util class is implemented to assist in readability within main"""

    def __init__(self):
        pass

    @staticmethod
    def manual_input():
        """A method that handles if the user chooses to manually
           enter the working data                            """
        input_data = list()

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
        return input_data

    @staticmethod
    def file_input():
        """A method that handles if the user chooses to use a file
           to handle inputing the file                         """
        input_data = list()

        file_name = input("Please enter file name:  ")
        validate = input(file_name + " --Correct?" + " Y (Yes) " +
                         " N (No):  ")
        validate = validate.lower()

        if validate == "y":
            try:
                with open(file_name, "r") as input_file:
                    for line in input_file:
                        line = line.strip()
                        line = int(line)
                        input_data.append(line)
            except Exception:
                print("File not found")

        else:
            print("Re-enter file name:  ")

        return input_data
