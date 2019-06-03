# exceptions occur when something goes wrong, whether it be 
# incorrect code or input. Exceptions stop the program immediately
# eg. dividing by 0.


# EXCEPTION HANDLING
# exceptions are dealt with by using "try/except" statements
# The try block contains code that may result in an exception
# If the exception occurs the try seciton is stopped and the
# except block is run instead. No error means no except being run.

# eg.

try:
    x = 7777
    y = 0
    Answer = (x/y)
    print (Answer)
except ZeroDivisionError: # this is the type of exception
    print ("You attempted to divide by zero. Don't do that.")



# try statements may have multiple different except blocks

try:
    print (x + "String")
    print (3/0)
except ZeroDivisionError:
    print ("Cannot divide by zero.")
except (ValueError, TypeError):
    print ("Error occured.")

# Except statements without a specific exception will catch all errors
# However they will catch unexpected errors and mask mistakes.

try:
    print (8 + "String")
except:
    print ("I am error.")

# FINALLY
# ensures some code will run when errors occur.
# always placed at the bottom of the try/except statement.

try:
    print (7 / "7")
except TypeError:
    print ("Type error.")
finally:
    print ("finally statement here.")

#try:
 #   print (x)
 #  print (x/0)
#except ZeroDivisionError:
 #   print (undefindVariable) # this causes an error. it has no value
#finally:
 #   print ("The 'finally' part is executed last.")
  #  print ("The program will still run with an uncaught exception in a preceding block.")


# RAISING EXCEPTIONS
# Raise will stop the program
# Specify the type of exception raised.
# The raised error report is customisable.

username = input("Enter username: ")
if username == ("Claus"):
    raise NameError ("Name is already taken")
else:
    print (username)


# ASSERTIONS
# "assert" tests an expression.
#  if the result is false an exception is raised

print (7)
assert ("7" + "7") == ("77")
print (77)
assert 7777 - 1 == 7777, "Doesn't = 7777" # 2nd argument is passed
print (7777)                              # to the AssertionError

# assertions are used to catch your own errors.
# exceptions are used to catch other people's errors