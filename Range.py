# range function creates a sequential list

example = list(range(7))
print (example)


# remembering that counts start at 0, not 1.
# the above print will print from 0 to 6.
# (7 digits total)

example2 = list(range(78))
print (example2)


# without the "list" qualifier, it will simply print the
# 2 figures at either end of the range
example3 = (range(11))
print (example3)


# this asks the program to print the 5th number (counts from 0)
example4 = list(range(5))
print (example4)
print (example4[4])

# an ARGUMENT is: a value passed to a function/method
# when calling it

# if a range is called with 1 argument (as above) it produces
# a list from 0 to the respective number.

# a range with 2 arguments produces values from the 1st up to
# but not including the 2nd

example5 = list(range(4,7))
print (example5)

example6 = (range(4,7))
print (example6)

# to get all boolean up in here:

print (range(14) == range(0,14)) # True

print (range(14) == range(0,13)) # False

# including a 3rd argument to a range will determine the
# interval size in a sequence

example7 = list(range(13,130,4))
print (example7)


example8 = list(range(3, 15, 3))
print(example8)
print (example8[0]) # prints the first digit in list which is 3