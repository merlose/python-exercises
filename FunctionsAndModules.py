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