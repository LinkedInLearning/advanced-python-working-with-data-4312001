# Example file for Advanced Python: Working With Data by Joe Marini
# using the map() function to transform data to another form

import json
import pprint


def squareFunc(x):
    return x**2


def toGrade(x):
    if (x >= 90):
        return "A"
    elif (x >= 80 and x < 90):
        return "B"
    elif (x >= 70 and x < 80):
        return "C"
    elif (x >= 65 and x < 70):
        return "D"
    return "F"


# define some sample sequences to operate on
nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
grades = (81, 89, 94, 78, 61, 66, 99, 74)

# TODO: use map to create a new sequence of values

# TODO: use sorted and map to change numbers to grades

# Use the filter on our data - let's filter out all seismic events that were *not* quakes
# open the data file and load the JSON
# with open("../../30DayQuakes.json", "r") as datafile:
#     data = json.load(datafile)


# filter the data down to the largest events
# def bigmag(q):
#     return q['properties']['mag'] is not None and q['properties']['mag'] >= 6


# results = list(filter(bigmag, data['features']))

# TODO: transform the largest events into a simpler structure
