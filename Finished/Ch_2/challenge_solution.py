# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import Counter, defaultdict


# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# use a defaultdict to categorize each event and count each one
totals = defaultdict(int)
for event in data['features']:
    totals[event['properties']['type']] += 1

for k, v in totals.items():
    print(f"{k:15}: {v}")
