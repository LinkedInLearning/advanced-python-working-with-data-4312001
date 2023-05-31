# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import defaultdict

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Print type of event and the number of events for that type.
totals = defaultdict(int)
for event in data['features']:
    totals[event['properties']['type']] +=1


for k,v in totals.items():
    print(f"{k:15}: {v}")