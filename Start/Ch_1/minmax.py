# Example file for Advanced Python: Working With Data by Joe Marini
# Demonstrates the usage of the min and max functions
import json


# Declare an array with some sample data in it
values = [3.0, 2.5, 5.1, 4.1, 1.8, 1.6, 2.2, 5.7, 6.1]
strings = ["one", "three", "five", "seven", "eleven", "eighteen"]


# TODO: The min() function finds the minimum value
print(f"the minimum value is: {min(values)}")
print(f"the minimum value is: {min(strings)}")

# TODO: The max() function finds the maximum value
# print(f"the maximum value is: {max(values)}")
# print(f"the maximum value is: {max(strings)}") # order alphabetically

# TODO: define a custom "key" function to extract a data field
# print(f"the maximum value is: {min(strings, key=len)}")
# print(f"the maximum value is: {max(strings, key=len)}") # by alphabetical order

# TODO: open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)
print(data["metadata"]["title"])
print(len(data["features"]))


def getmag(dataitem):
    magnitute = dataitem["properties"]["mag"]
    if magnitute is None:
        magnitute = 0
    return float(magnitute)



print(min(data["features"], key=getmag))
