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

# 1: We can just use the provided data, or we can use len() to get the length of the "features"
print(f"Total quakes: {data['metadata']['count']}")

# 2: 

# 3: This is a straightforward filtering process
def feltreport(q):
  f = q["properties"]["felt"]
  return (f is not None and f >= 100)

feltreports = list(filter(feltreport, data["features"]))
print(f"Total quakes felt by at least 100 people: {len(feltreports)}")

# 4: 

# 5: We can use the max function here to find the maximum # of felt reports
def getfelt(q):
  f = q["properties"]["felt"]
  if f is not None: return f
  return 0

mostfeltquake = max(data["features"], key=getfelt)
print(f"Most felt reports: {mostfeltquake['properties']['title']}, reports: {mostfeltquake['properties']['felt']}")
