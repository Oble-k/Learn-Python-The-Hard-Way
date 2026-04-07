#Symbol review
# I'm gonna try some keywords to learn what they do:
# ASSERT
print("-----ASSERT-----")

# If the content inside of assert is fase, an exception will be raised, in this case the AssertionError
assert(1==1),"aaaa estas sequit" #nothing
# assert(1==2) #AssertionError
print("Hey")
# assert False, "Aaaaa te bañastes"

# AS
print("-----AS-----")
# There is no as statement. As is used to add clauses to a few different statements
# The as keyword allows to create an alias.
# But it seems to only work with modules.
# We import calendar and rename it as f, so that we may call it using the alias instead of the full name.
# If we use the "as" keyword, we have to use the alias
import calendar as f
for i in range (13):
    print(f.month_abbr[i])
# print(calendar.month_abbr[2])

# BREAK
print("-----BREAK-----")
# Break is used to inmediately exit a loop when a certain condition is met
# Is a way to exit a loop prematurely
for num in range(10):
    if num == 5:
        print("Exiting the loop, wee reached number {}".format(num))
        break
    print(num)

# CLASS
print("-----CLASS-----")
# A class is a code template for creating objects. Objects have member variables and have behaviour associated with them.
# In python a class is created by the keyword "class".
class Snake:
    name = "python"
    length = 2.5
    weight = 85
    pass
snake = Snake()
print(Snake())
print(snake.name)
print(snake.length)
print(snake.weight)

# CONTINUE
print("-----CONTINUE-----")
# The continue keyword is used to end the current iteration in a for loop,
# and continues to the next.
total = 0

for number in range(-10, 10):
    if number < 0:
        print("The number is {}. It is negative. It will not be added to the total.".format(number))
        continue #This makes it so that it will only add the numbers which are positive
    total += number
print(total)

# DEL
# del, deletes an item from a list
print("-----DEL-----")
n_list = [1, 2, 3, 4, 5]
print(n_list)
del n_list[2]
print(n_list)

# TRY
print("-----TRY-----")
# the try blocks lets you test a block of code for errors

x = 7
try:
    print(x)
except:
    print("An exception occurred")

# EXCEPT
print("-----EXCEPT-----")
# the except block lets you handle the error

try:
    print(y)
except:
    print("An exception occurred")

# ELSE
print("-----ELSE-----")
# The else block lets you execute code when there is no error

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# FINALLY
print("-----FINALLY-----")
# The finally block lets you execute code, regardless of the try and except blocks
print("\tThis one goes right:")
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
print("\tThis one goes wrong:")
try:
  print(y)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# RAISE
print("-----RAISE-----")
# raise is the way in which it is possible to throw an exception if a condition occurs.
# x = -1
# if x < 0:
#     raise Exception("No numbers below zero!")
