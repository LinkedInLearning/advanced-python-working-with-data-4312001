# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("C:/Users/Vani/Downloads/advanced-python-working-with-data-4312001-main/advanced-python-working-with-data-4312001-main/30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)
    
 #1
    print(len(data["features"]))
#2
    print(sum(quake["properties"]["felt"] is not None and quake["properties"]["felt"] >= 100 for quake in data["features"]))
#3

    def quakeFelt(quake):
        if quake["properties"]["felt"] is not None :
            return True
        return False
    
    quakeFeltbyMost = max(data["features"], key=quakeFelt)
    print(quakeFeltbyMost["properties"]["title"])
    print(quakeFeltbyMost["properties"]["felt"])
  
#4
    def getsig(quake):
        s = quake["properties"]["sig"]
        if s is not None:
            return s
        return 0
    
    sigevents = sorted(data["features"], key=getsig, reverse=True)
    for i in range (0,10):
        print(f"Event :{sigevents[i]['properties']['title']}, significance- {sigevents[i]['properties']['sig']}")
