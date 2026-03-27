# Functions and Variables
# NOTE:The variables in your function are not connected to the variables in your script
# NOTE: If you cann use = to name something, you can usually pass it to as an argument
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
# NOTE: It is possible to have a global variable with the same name as a function
# However it is considered bad practice. Avoid it if possible

print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math")
# Here it adds 100 to the 10 original value of cheese, and 1000 to the original 50 crackers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def joints_and_rum(joint_count, rum_bottles):
    print(f"    There are {joint_count} joints left")
    print(f"    There are just {rum_bottles} of rum left")
    print("    We won't make it back from the sea")

print("Using numbers directly for both items, joints and rum bottles:")
joints_and_rum(3, 1)

print("Using variables:")

joint_count = 10
rum_bottles = 2
joints_and_rum(joint_count, rum_bottles)

print("Asking the user to give us the amount of joints left:")
joint_count = input("How many joints can you see (only joints)?: ")
rum_bottles = 2
joints_and_rum(joint_count, rum_bottles)

print("Asking only about rum bottles: ")
joint_count = 3
rum_bottles = input("How many rum bottles you got?: ")

print("Using the input function at the same time that we call the function:")
joints_and_rum(input("How many joints would you have? "), input("\nHow many rum bottles you got left? "))

# There is a very large limit of arguments a function can have.
# The practical limit is about 5 arguments
# It is possible to call a function within a function