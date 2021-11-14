# py file for City List
import os
import sys
import random


def get_city_list():

    # open the file with cities in read mode
    # getting the name of the directory
    # where the this file is present.
    current = os.path.dirname(os.path.realpath(__file__))

    # Getting the parent directory name
    # where the current directory is present.
    parent = os.path.dirname(current)

    # adding the parent directory to
    # the sys.path.
    sys.path.append(parent)
    filename = open("py_files/cityList.csv", "r")

    # creating empty list to store the data
    cities = []

    # iterating over each row and append values to the list
    for line in filename:
        cities.append(line.strip())

    # shuffle the list
    random.shuffle(cities)

    # return list
    return cities
