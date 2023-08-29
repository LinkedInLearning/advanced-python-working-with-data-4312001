# Example file for Advanced Python: Working With Data by Joe Marini
# demonstrates how to serialize data to a CSV file

import csv
import json
import datetime

# read in the contents of the JSON file
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


def isbig(x):
    mag = x["properties"]["mag"]
    return mag is not None and mag > 5


# Filter the data by quakes that are larger than 5 magnitude
largequakes = list(filter(isbig, data["features"]))

# TODO: Create the header and row structures for the data
header = ["Place", "Magnitude", "Link", "Date"]
rows = []

# TODO: populate the rows with the resulting quake data
for quake in largequakes:
    thedate = datetime.date.fromtimestamp(
        int(quake["properties"]["time"]/1000))
    rows.append([quake["properties"]["place"],
                quake["properties"]["mag"],
                quake["properties"]["url"],
                thedate])
# TODO: write the results to the CSV file
with open("largequakes.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(header)
    writer.writerows(rows)
