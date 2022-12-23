# Demonstrate the usage of defaultdict objects

from collections import defaultdict


# define a list of items that we want to count
fruits = ['apple', 'pear', 'orange', 'banana',
          'apple', 'grape', 'banana', 'banana']

# use a dictionary to count each element
fruitCounter = defaultdict(int)

# Count the elements in the list
for fruit in fruits:
    fruitCounter[fruit] += 1

# print the result
for (k, v) in fruitCounter.items():
    print(k + ": " + str(v))
