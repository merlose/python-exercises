# the variable below counts up until the condition is false

number = 1

while number <= 5:
    print (number)
    number = number + 1

print ("Done...")

# don't forget colons at ends of statements

example2 = 50

while example2 >= 1:
    print (example2)
    example2 = example2 / 5

print ("Finish")


floatyPythons = 6

while floatyPythons <= 10000: 
    print ("%.1f" % floatyPythons)
    floatyPythons = floatyPythons * 1.5

print ("Enough floatyPythons")

# to print results to a number of decimal places:
# use ' "%.2f" % ' variable
# (2 is to 2 decimal places in this example)

# infinite loop
    # these never stop running. their condition is always True

print ("break")

# break
    # break ends a while loop prematurely

bork = 0
while 1 == 1:               # which is always
    print (bork)            # prints variable's value
    bork = bork + 1         # takes value and adds 1 repeatedly
    if bork >= 5:               # because of the "while"
        print ("Borken")    # once value >= 5 print this
        break               # break command halts loop
print ("Done borked.")


print ("continue")

# continue jumps to the next line of the loop
    # instead of stopping it

cont = 0
while True:
    cont = cont + 1
    if cont == 2:
        print ("No twos here...")
        continue
    if cont == 5:
        print ("Borking")
        break
    print (cont)
print ("Done")

# use of "continue" outside of loops will error