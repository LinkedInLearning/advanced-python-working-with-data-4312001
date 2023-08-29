# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime

from itertools import islice


def take(n, iterable):
    """Return the first n items of the iterable as a list."""
    return list(islice(iterable, n))


# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD


def getsig(q):
    significance = q["properties"]["sig"]

    if (significance is None):
        significance = 0
    return float(significance)


def gettime(q):
    time = q["properties"]["time"]

    if (time is None):
        time = 0
    return float(time)


def getmaplink(q):
    lat = q["geometry"]["coordinates"][1]
    lng = q["geometry"]["coordinates"][0]
    link = f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"
    return link


header = ["Magnitude", "Place", "Felt Reports", "Date", "Google Map Link"]
rows = []

sigs = sorted(data["features"], key=getsig, reverse=True)

sig_forty = take(40, sigs)

sigs = sorted(sig_forty, key=gettime, reverse=True)

for i in range(0, 40):
    thedate = datetime.date.fromtimestamp(
        int(sigs[i]["properties"]["time"]/1000))
    maplink = getmaplink(sigs[i])
    rows.append([sigs[i]["properties"]["mag"],
                 sigs[i]["properties"]["place"],
                 0 if sigs[i]["properties"]["felt"] is None else sigs[i]["properties"]["felt"],
                 thedate,
                 maplink
                 #                sigs[i]["properties"]["url"]
                 ])

with open("sigquakes.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(header)
    writer.writerows(rows)
