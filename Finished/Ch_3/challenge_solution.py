# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: serialize earthquake data to a file

import json


# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)
