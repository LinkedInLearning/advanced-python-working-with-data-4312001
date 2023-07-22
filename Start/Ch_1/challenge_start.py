# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json

# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# use the provided data or get the length of the "features"
print(f"total quakes: {data['metadata']['count']}")


#  this is a filtering process
def feltreport(q):
    f = q["properties"]["felt"]
    return f is not None and f >= 100


feltreports = list(filter(feltreport, data["features"]))
print(f"total quakes felt by at least 100 people: {len(feltreports)}")


def getfelt(q):
    f = q["properties"]["felt"]
    if f is not None:
        return f
    return 0


mostfeltquake = max(data["features"], key=getfelt)
print(f"most felt reports: {mostfeltquake['properties']['title']}, reports: {mostfeltquake['properties']['felt']}")


def getsig(q):
    s = q["properties"]["sig"]
    if s is not None:
        return s
    return 0


sigevents = sorted(data["features"], key=getsig, reverse=True)
print("the 10 most significant events were:")
for i in range(0,10):
    print(
        f"Event: {sigevents[i]['properties']['title']}, Significance: {sigevents[i]['properties']['sig']}"
    )
