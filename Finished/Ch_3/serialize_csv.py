# Example file for Advanced Python: Working With Data by Joe Marini
# demonstrates how to serialize data to a CSV file

import csv
import json
import datetime

# read in the contents of the JSON file
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


def isbig(x):
    mag = x["properties"]["mag"]
    return mag is not None and mag > 5


# Our code will create a CSV file
largequakes = list(filter(isbig, data["features"]))
print(len(largequakes))
header = ["Place", "Magnitude", "Link", "Date"]
rows = []
for quake in largequakes:
    thedate = datetime.date.fromtimestamp(
        int(quake["properties"]["time"])/1000)
    rows.append([quake["properties"]["place"], quake["properties"]
                ["mag"], quake["properties"]["url"], thedate])

with open("largequakes.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(header)
    writer.writerows(rows)
