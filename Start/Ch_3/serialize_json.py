# Example file for Advanced Python: Working With Data by Joe Marini
# demonstrates how to serialize data to a JSON file

import json
import datetime


# read in the contents of the JSON file
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


def isbig(x):
    mag = x["properties"]["mag"]
    return mag is not None and mag > 6


# TODO: define a function to transform complex JSON to simpler JSON


# filter the data to only include large quakes
largequakes = list(filter(isbig, data["features"]))
# TODO: transform the data to a JSON format we want to save

# TODO: use the dumps() function to write json to a string

# TODO: use the dump() function to write json to a file
