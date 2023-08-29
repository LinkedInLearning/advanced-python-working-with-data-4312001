# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import Counter
from collections import defaultdict


# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

quakecounter = defaultdict(int)

for q in data['features']:
    quakecounter[q['properties']['type']] += 1

print(quakecounter.items())
for k, v in quakecounter.items():
    print(f"{k:30} : {v}")

