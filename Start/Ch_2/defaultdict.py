# Demonstrate the usage of defaultdict objects

from collections import defaultdict


# define a list of items that we want to count
fruits = ['apple', 'pear', 'orange', 'banana',
          'apple', 'grape', 'banana', 'banana']

# TODO: use a dictionary to count each element
# Careful, any key that wasn't explicitly added t othe dictionary will be added when you run default dict.
fruitCounter = defaultdict(lambda: 100)

# TODO: Count the elements in the list
for fruit in fruits:
    fruitCounter[fruit] += 1

# TODO: print the result
print(fruitCounter)
