# Example file for Advanced Python: Working With Data by Joe Marini
# read data from a CSV file into an object structure

import csv
import pprint


# read the contents of a CSV file into an object structure
result = []

# open the CSV file for reading
with open("largequakes.csv", "r") as csvfile:
    # create the reader object
    reader = csv.reader(csvfile)

    # does the file contain headers?
    sniffer = csv.Sniffer()
    sample = csvfile.read(1024)
    csvfile.seek(0)
    if (sniffer.has_header(sample)):
        next(reader)

    # iterate over each row
    for row in reader:
        # print(row)

        # add the data to our list
        result.append({
            "place": row[0],
            "magnitude": row[1],
            "date": row[2],
            "link": row[3]
        })

pprint.pp(result)
