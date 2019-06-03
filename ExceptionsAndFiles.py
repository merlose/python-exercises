# exceptions occur when something goes wrong, whether it be 
# incorrect code or input. Exceptions stop the program immediately
# eg. dividing by 0.


# EXCEPTION HANDLING
# exceptions are dealt with by using "try/except" statements
# The try section contains code that may result in an exception
# If the exception occurs the try seciton is stopped and the
# except section is run instead. No error means no except being run.

# eg.

try:
    x = 7777
    y = 0
    Answer = (x/y)
    print (Answer)
except ZeroDivisionError:
    print ("You attempted to divide by zero. Don't do that.")