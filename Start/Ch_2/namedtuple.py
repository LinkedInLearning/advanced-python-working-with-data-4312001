# Demonstrate the usage of namdtuple objects

import collections


# TODO: create a Point namedtuple
Point = collections.namedtuple("Point", "x y")
p1 = Point(10, 20)
p2 = Point(30, 40)
print(p1, p2)

print(p1.x, p2.y)
# TODO: use _replace to create a new instance
p1 = p1._replace(x=100)

print(p1)

# Useful for creating a lightweight, immutable class that is easily readable and isn't too much code.
# limitations: default argument values can't be used so for a large number of variables a normal class may be better.
