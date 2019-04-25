#lists

#square brackets. separate with commas:

words = ["Hello", "World", "!"]

print(words[1])
print(words[2])
print(words[0])
print(words[2])

# count up from 0. not 1

# empty list will print square brackets...
#don't know why this was in a tutorial...

empty_list = []
print(empty_list)

# lists can be nested within lists

list = [0, ["Hat","Dogs","Cloud"]]
print (list[1])
print (list[0])
print (list[1][1])
print (list[1][2])
print (list[1][0])

# to print individual characters of a string:

borf = "Tiger"
print (borf[4]) # prints 5th character "r"

# Reassign certain indexes in a list

temp = [-2,0,3,7,13] # remember it is [SQUARE BRACKETS]
temp[1]=-1
print (temp)

summer = ["So hot!","Far too hot!","Blazing heat!"]
print (summer)
print (summer[1])

summer[1]=("Not far too hot enough!")
print ("Addendum")
print (summer)
print (summer[1])

# Add and multiply lists

nos = [2,4,6]
print (nos)
print (nos + ["Deer antler"])
print (nos * 4)

# "in" operator. Used to see if an item is in a list.
    # reports True if the item appears once or more. False if not.

list_60 = ["Hippos","Deer","Frogs"]
print ("Hippos" in list_60)
print ("Toads" in list_60)

# "not" operator. Checks if an item is NOT in a list
    # as above reports True or False

print ("Frogs" not in list_60)
print ("Toads" not in list_60)

# "append" method. Adds an item to the end of a list
    # Methods are like functions but they work on objects.

print (list_60)
list_60.append ("Dragonflies") # note the . before append
print (list_60)

# "len" function. Gets number of items in a list
print ("Items in list_60:")
print (len(list_60))
print ("Items in Summer:")
print (len(summer))

# "insert" method. Like append. Use "(n, xxxxx)" where n is a
    # position in the list

print (list_60)
list_60.insert (1, "oh")    # again noting the . before insert
list_60.insert (3, "not enough")
list_60.insert (5, "and too many")
print (list_60)

list_61 = ["Hippo-people", "Jaguars", "Macaws"]
print (list_61)
list_61.append("Flying squirrels")
print (list_61)
list_61.insert (2,"Shrimp")
print (list_61)
print ("Items in list_61:")
print (len(list_61))

# "index" method. Finds the 1st instance of an item in a list
    # and returns its index

print (list_61)
print ("Macaw index =")
print (list_61.index("Macaws")) # to get index for macaws
print ("Shrimp index =")
print (list_61.index("Shrimp"))

    #and to error with something that isn't in list_61:
    # print ("Human-hippos index =")
    # print (list_61.index("Human-hippos"))