types_of_people = 100
x = f"There are {types_of_people} types of people." #Creates a string variable, which will change depending on types_of_people
# In the previous line there is 1 string inside another string
binary = "binary" #string variable, it is the same as its name
do_not = "don't" #string variable, not the same as its name
#The next string variable depends on the binary and the do_not variable
#Here there are 2 strings inside 1 string
y=f"Those who know {binary} and those who {do_not}"
#The f" at the beginning makes its so that it is not needed to write it on the print command
print(x)
print(y)
#I believe that there are multiples f" required if you want to embed a string unto another in a recursive manner
# The next print will change with x, as well as x will change with types_of_people
#The f and the {} tell python that the string needs to be formatted
print(f"I said: {x}. ")
#The next print will change with y, and y will change with binary and do_not
print(f"I also said: {y}.")
#This sets a variable as false
hilarious = True
#string variable, this time with the {} characterss empty, this requires the .format clause to work, otherwise python would consider it a regular set of charactes
joke_evaluation = "Isn't that joke so funny?! {}"
#There is a different way to print what the next line of code prints
print(joke_evaluation.format(hilarious))
print(f"{joke_evaluation}{hilarious}.") #It seems that it also prints the {} of the joke_evaluation
w="This is the left side of..."
e="a string with a right side."
#In this case the operator + doesn't work as a sum, rather as a concatenator, which means that it puts the puzzle pieces in the order in which they are written
print(w + e)
print(f"{w}{e}.")
#The next line will print the 2 strings in the opposite order that it is to be expected.
print(e + w)
