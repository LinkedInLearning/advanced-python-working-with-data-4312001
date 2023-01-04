# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: serialize earthquake data to a file

import json
import csv
import datetime


# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD


def getsig(x):
    sig = x["properties"]["sig"]
    return 0 if sig is None else sig


significantevents = sorted(data["features"], key=getsig)
significantevents.sort(key=getsig, reverse=True)
header = ["Magnitude", "Place", "Felt Reports", "Date", "Link"]
rows = []

for i, event in enumerate(significantevents):
    if i == 40:
        break

    thedate = datetime.date.fromtimestamp(
        int(event["properties"]["time"]) / 1000)
    lat = event["geometry"]["coordinates"][1]
    long = event["geometry"]["coordinates"][0]
    gmaplink = f"https://maps.google.com/maps/search/?api=1&query={lat}%2C{long}"

    rows.append([event["properties"]["mag"],
                event["properties"]["place"],
                0 if event["properties"]["felt"] is None else event["properties"]["felt"],
                thedate,
                gmaplink])

with open("significantevents.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(header)
    writer.writerows(rows)
