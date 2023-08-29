# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json
import pprint

# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each


# MY ATTEMPT
# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# total = data["metadata"]["count"]
# print(f"In total, there were: {total} quakes")

# felt100 = sum(quake["properties"]["felt"] is not None and quake["properties"]["felt"] >= 100
#          for quake in data["features"])
# print(f"{felt100} quakes were felt by more than 100 people")

# def getfelt(q):
#    feltby = q["properties"]["felt"]
#    if (feltby is None):
#         feltby = 0
#     return float(feltby)

# maxfelt = max(data["features"], key = getfelt)

# #print(maxfelt)

# def simplify(q):
#     return{
#         "place": q["properties"]["place"],
#         "felt": q["properties"]["felt"]
#     }

# maxfelt = simplify(maxfelt)
# #pprint.pp(maxfelt)
# numberfelt = maxfelt["felt"]
# placefelt = maxfelt["place"]
# print(f"The quake felt by the most people ({numberfelt}) occurred in {placefelt}")

# def getsig(q):
#     sig = q["properties"]["sig"]
#     if (sig is None):
#         sig = 0
#     return float(sig)

# data["features"].sort(key = getsig, reverse = True)

# print("the top 10 most significant events were:")

# for i in range(0,10):
#     print(data["features"][i]["properties"]["sig"])
#     print(data["features"][i]["properties"]["place"])


# HIS ANSWER:

# 1: We can just use the provided data, or we can use len() to get the length of the "features"
print(f"Total quakes: {data['metadata']['count']}")


# 2: This is a straightforward filtering process
def feltreport(q):
    f = q["properties"]["felt"]
    return (f is not None and f >= 100)


feltreports = list(filter(feltreport, data["features"]))
print(f"Total quakes felt by at least 100 people: {len(feltreports)}")


# 3: We can use the max function here to find the maximum # of felt reports
def getfelt(q):
    f = q["properties"]["felt"]
    if f is not None:
        return f
    return 0


mostfeltquake = max(data["features"], key=getfelt)
print(
    f"Most felt reports: {mostfeltquake['properties']['title']}, reports: {mostfeltquake['properties']['felt']}")


# 4: This is a sorting operation
def getsig(q):
    s = q["properties"]["sig"]
    if s is not None:
        return s
    return 0


sigevents = sorted(data["features"], key=getsig, reverse=True)
print("The 10 most significant events were:")
for i in range(0, 10):
    print(
        f"Event: {sigevents[i]['properties']['title']}, Significance: {sigevents[i]['properties']['sig']}")
