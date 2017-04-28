""" This file is part of the File I/O exercise.

It should be used with the two input files, fruits_1.txt and fruits_2.txt."""

def open_and_read_file(filename):
    """Opens file as a file object and returns list of contents."""

    fruit_file = open(filename)
    fruit_data = fruit_file.read()
    fruit_list = fruit_data.split()
    fruit_file.close()

    return fruit_list


def compare(list1, list2):
    """Takes in two lists and returns a list of items in common. """

    list_in_common = []

    for item in list1:
        if item in list2:
            list_in_common.append(item)

    return list_in_common


def output_to_user(list):
    """Takes the list of items in common, and outputs it in one sentence. """

    print ""

# Call your functions all the way at the bottom, after they've been defined.
list1 = open_and_read_file("fruits_1.txt")
list2 = open_and_read_file("fruits_2.txt")

items_in_common = compare(list1, list2)
print items_in_common

