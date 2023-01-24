# Demonstrate the usage of defaultdict objects

from collections import defaultdict


# define a list of items that we want to count
fruits = ['apple', 'pear', 'orange', 'banana',
          'apple', 'grape', 'banana', 'banana']

# TODO: use a dictionary to count each element
fruitCounter = dict()

# TODO: Count the elements in the list
for fruit in fruits:
    fruitCounter[fruit] += 1

# TODO: print the result
