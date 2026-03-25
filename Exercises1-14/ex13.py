from sys import argv
#read WYSS section for how to run this
script = argv

# first = input("Name of the first variable? ")  #This allows the user to put a string in the variables
# second = input("Name of the second variable? ")
# third = input("Name of the third variable? ")

first = int(input("Value of the first variable? "))  #This allows the user to put a numerical value (integer) the variables
second = int(input("Name of the second variable? "))
third = int(input("Name of the third variable? "))

print("The script is called: ", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)
# Line 1: we have an import, this is how you add features to your script
# from the python feature set. Instead of give you all the features,
# python will ask you to say what are you planning to use
# argv stands for argument variable, this variable holds
# the arguments you pass to your python script when you run it.
# Line 3 "unpacks" argv so that rather than holding all the arguments it gets assigned to four variables
# you can work with.
# "Take whatever is in argv, unpack it, and assign it to all these variable on
# the left in order
# Features==modules
#its important to run this on the terminal via python3 script.py arg1 arg2 arg3
