# if statements eh

if (6 > 5):
    print ("Yes, 6 is greater than 5") 
print("Program ended")

number = 3

if number >= 2: 
    print ("Number is greater than 2") 
    if number <= 10: 
        print ("Number is between 2 & 10")

print("Program ended")

number = 6 
if number >= 8: 
    Print ("Number is greater than or equal to 8.") 
else:
    print ("Number is less than 8.")
print("Program ended")

# if statements chained together using "elif" (else/if) and ending with else

print ("if statements chained together using 'elif'")

num = 8

if num == 5:
    print ("num = 5")
elif num == 12:
    print ("num - 12")
elif num == 7:
    print ("num = 7")
else:
    print ("num is not 5, 12 or 7")

# boolean logic operator: "and". Evaluating multiple conditions true or false

print ("boolean logic operators:")
print ("and:")

print (1 == 1 and 2 == 2) # both must be true to evaluate as True

print (1 == 1 and 2 == 3) # MUST be within ONE set of brackets

print (1 != 2 and 2 != 3)

print (1 < 2 and 2 < 3)

print (1 != 1 and 2 == 2 and 3 > 4)

# operator "or". Evaluates True even if only 1 of its arguments is true.

print ("or:")

print (1 == 1 or 2 == 3) # evaluates True because 1st is true even though 2nd is not

print (1 >= 2 or 3 != 3) # evaluates False only when all arguments are false


# operator "not". inverts 1 argument

print ("not:")

print (not 1 == 1) # evaluates the true condition as False

print (not 2 < 1) # evaluates the false condition as True
