# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were larger than magnitude 4? Less than 4?
# 3: How many quakes were felt by at least 100 people?
# 4: Classify the quakes as small (< mag 3.0), medium (3.0 to 5.0), and large (> 5.0).
# How many were there of each (small, medium, large)?
# 5: Print the name of the place whose quake was felt by the most people, with the # of reports

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)
