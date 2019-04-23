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

list = [0, ["Hat", "Dogs", "Cloud"]]
print (list[1])
print (list[0])
print (list[1][1])
print (list[1][2])
print (list[1][0])

# to print individual characters of a string:

borf = "Tiger"
print (borf[4]) # prints 5th character "r"

# Reorder lists

temp = [-2,0,3,7,13] # remember it is [SQUARE BRACKETS]
temp[1]=-1
print (temp)

summer = ["So hot!","Far too hot!","Blazing heat!"]
print (summer)

summer[1]=("Not far too hot enough!")
print ("Addendum")
print (summer)
print (summer[1])

# testing...