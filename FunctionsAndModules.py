# def

def hippo():
    print (7 * 7) 
hippo()

def hippo2():
    print (4 + 26)
hippo2()

    # 'def' creates your own function
    # ensure to include (): when creating, and () when calling

    # these do not work as variables
    # you obviously cannot call them before they have been defined

# most functions take arguments (something in the parentheses)
# e.g.

def add_exclamation (panic): # descriptive variable "panic"
    print (panic + "!!!")

add_exclamation ("Is someone out there?")
add_exclamation ("It's getting dark")
add_exclamation ("I think it knows where we are")

# a simple function to find 75% of a value:

def three_quarters(x):
    print (0.75 * x)

three_quarters (100)

# multiple arguments may be separated by commas:

def multiply(x,y):
    print (x * y)

multiply (15,8)

# variables CAN be created inside defs
# but they can't be referenced outside of the function

def add_vat(n):
    n = n + (n * 0.2)
    print (n) # needs this print (variableName) for some reason???

print ("Before tax: 7.7. After tax:")
add_vat(7.7)

# 'return' produces a value that can be used further:

def highest(o,p):
    if o >= p:
        return o + (o * 0.2) # returns o + 20% of its value
    else:
        return p + (p * 0.2) # returns p + 20% of its value

print (highest(17,77))
someOtherVariable = highest(66,16)
print (someOtherVariable)

# any code after the return statement will not be used.
# again, return cannot be used outside of a def


# FUNCTIONS

# functions are created differently to variables,
# they can be assigned and reassigned to variables
# and later referenced by the new variable names:

def bahamut(x,y):
    return x / y

a = 16
b = 4
operation = bahamut
print ("16 / 4")
print (operation(a,b))

    # above: says bahamut is a function that contains x and y
    # it returns x divided by y when called
    #then we set 3 new variables: a, b and operation
    # a and b contain numbers. operation is a variable for bahamut
    # when printing operation we have to include the arguments
    # the arguments (a,b) work in place of bahamut's (x,y)

print (bahamut(a,b)) # using bahamut itself instead of the variable
                     # 'operation' produces the same result

borf = 200
dog = 5
print ("200 / 5")
print (operation(borf,dog))

print ("200 / 4 * 200 / 5")
print (operation(borf,b)*operation(borf,dog))

output = operation(a,b) # here showing you can chain variables
print (output)

# Functions can also be used as arguments of other functions:

def gains(g, h):
  return g + h

def do_twice(func, g, h):
  return func(func(g, h), func(g, h))

g = 5
h = 10

print(do_twice(gains, g, h))

# Modules
 # pieces of code written to fulfill tasks. e.g. RNG, maths ops etc
 
 # 3 main types:
    # pre-installed modules in Python's standard library.
    # modules installed from external sources
    # and modules you write yourself

import random

for i in range(7):
    value = random.randint(70, 79)
    print(value)

# take the form "from module_name import var",
# then var can be used as if it were defined normally in your code.

from math import pi     # imports only the pi constant
print (pi)              # from the math module

# trying to import an unavailable module will cause an ImportError

# rename modules (eg. if they have long or confusing names)
# by using "as"

from math import sqrt as squareRoot # renaming "sqrt"
print (squareRoot(250)) # using its new name in 2 examples
print (squareRoot(pi))

# complete documentation of python's standard library can be found online

# a way to install third party modules is a program called "pip"
# these are stored on the Python package index (PyPI)
# to install, go to the command Command Prompt and enter
# "pip install library_name"

print ("scribble pad")

def pebble(k):
    for j in range(k):
        print (j)
        return
pebble(10)

def sand(b):
    res = 0
    for v in range(b):
        res += v    # SAME AS: res = res + v
    return res
print (sand(4))     # runs the loop 4 times

# therefore:
#1:     res = 0 (res) + 0 (v)
#2:     res = 0 (res) + 1 (v 2nd loop)
#3:     res = 1 (0+1) + 2 (v 3rd loop)
#4:     res = 3 (1+2) + 3 (v 4th loop)

# res is not inside the loop so it doesn't reset to 0 each loop