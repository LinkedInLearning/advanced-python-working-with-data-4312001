# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json
import pprint


# for this challenge, we're going to summarize the earthquake data as follows:

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


def quake(q):
    if q["properties"]["type"] == "earthquake":
        return True
    return False


def get_felt(record):
    felt = record["properties"]['felt']
    if (felt is None):
        felt = 0
    return float(felt)


def felt_filter(q):
    felt_quake = q['properties']['felt']
    if felt_quake is not None and felt_quake >= 100:
        return True
    return False


def get_sig(q):
    sig = q['properties']['sig']
    if sig is not None:
        return float(sig)
    return 0.0


def get_most_significant(events):
    events["features"].sort(key=get_sig, reverse=True)
    return events["features"][0]


# 1: How many quakes are there in total?
quakes = list(filter(quake, data['features']))
print(f"Total number of quakes: {len(quakes)}")
print(f"Total number of events: {data['metadata']['count']}")

# 2: How many quakes were felt by at least 100 people?
popular = list(filter(felt_filter, quakes))
print(f"Number of quakes felt by at least 100 people: {len(popular)}")

# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
most_felt = max(data["features"], key=get_felt)
print(
    f"Most felt quake at {most_felt['properties']['title']}, reports: {most_felt['properties']['felt']}")


# 4: Print the top 10 most significant events, with the significance value of each
sig_events = sorted(data["features"], key=get_sig, reverse=True)
for i in range(0, 10):
    print(
        f"Event: {sig_events[i]['properties']['title']}, Significance: {sig_events[i]['properties']['sig']}")
