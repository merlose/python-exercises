# 'for' in python behaves like 'foreach' in other languages

# iteration - performing code on each item in a list

list = ["dogs","macaws","geckos","tortoises"]
print (list)
for word in list:
    print (word + "?")

    # the above will add a question mark to each item
    # the variable we created here is 'word'
    # this variable can be named anything you like


for heck in range (7):
    print ("seven")

    # this demonstrates repeating code a number of times
    # no need to call 'list' on the range object when used
    # in a 'for' loop because nothing is being indexed