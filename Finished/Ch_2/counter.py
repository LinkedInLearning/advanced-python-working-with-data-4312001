# Demonstrate the usage of Counter objects

from collections import Counter


# list of students in class 1
class1 = ["Bob", "James", "Chad", "Darcy", "Penny", "Hannah",
          "Kevin", "James", "Melanie", "Becky", "Steve", "Frank"]

# list of students in class 2
class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
          "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

# Create a Counter for class1 and class2
c1 = Counter(class1)
c2 = Counter(class2)

# How many students in class 1 named James?
print(c1["James"])

# How many students are in class 1?
print(sum(c1.values()), "students in class 1")

# Combine the two classes
c1.update(class2)
print(sum(c1.values()), "students in class 1 and 2")

# What's the most common name in the two classes?
print(c1.most_common(3))

# Separate the classes again
c1.subtract(class2)
print(c1.most_common(1))

# What's common between the two classes?
print(c1 & c2)
