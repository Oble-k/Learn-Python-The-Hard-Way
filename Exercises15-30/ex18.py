#Names, Variables, Code, Functions
def print_two(*args):
    arg1,arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
# What does the asterisks in *args do?
# It tells python to take all the arguments to the function and then put them in args as a list.
# It is really similar to argv but for functions
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothing.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

#def==define
# define allows us to make a function and give it a name. The name can be anything.
# a function should have a short name that saws what it does