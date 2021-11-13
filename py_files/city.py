# py file for City List

import random

def get_city_list():

    # open the file with cities in read mode
    filename = open("cityList.csv", "r")

    # creating empty list to store the data
    cities = []

    # iterating over each row and append values to the list
    for line in filename:
        cities.append(line.strip())

    # shuffle the list
    random.shuffle(cities)

    # return list
    return cities
