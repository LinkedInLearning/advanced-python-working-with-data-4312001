# Example file for Advanced Python: Working With Data by Joe Marini
# using the filter() function to filter a data set


def filterEvens(x):
  # filters out even numbers and keeps odd numbers
  if x % 2 == 0:
      return False
  return True


def filterUppers(x):
  # filters out upper-case letters and keeps lower case letters
  if x.isupper():
      return False
  return True


# define some sample sequences to operate on
nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
chars = "abcDeFGHiJklmnoP"
grades = (81, 89, 94, 78, 61, 66, 99, 74)

# use filter to remove items from a list
odds = list(filter(filterEvens, nums))
print(odds)

# use filter on non-numeric sequence
lowers = list(filter(filterUppers, chars))
print(lowers)
