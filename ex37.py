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
# print(f"This snake is known as a {snake.name}")
# print(f"Snake's length is {snake.length}")
