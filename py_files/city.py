# py file for City List
import os
import sys
import random


class city_manager:
    def __init__(self):
        # find the location of the csv file
        current = os.path.dirname(os.path.realpath(__file__))
        parent = os.path.dirname(current)
        sys.path.append(parent)
        # open the file with cities in read mode
        filename = open("py_files/cityList.csv", "r")

        # initialize and fill list
        self.cities = self.fill_list(filename)

        # shuffle the list
        random.shuffle(self.cities)

    # function to parse a string from a file and turn it into a list of cities
    def fill_list(self, filename):
        # iterating over each row and append values to the list
        cities = []
        for line in filename:
            cities.append(line.strip())

        return cities

    def get_city_list(self):
        # return list
        return self.cities

    def get_city(self):
        # return first item from city list after shuffling the list
        random.shuffle(self.cities)

        return self.cities[0].lower().capitalize()


if __name__ == "__main__":
    city_manager()
