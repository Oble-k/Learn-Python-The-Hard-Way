#Prompting and Passing
from sys import argv

script, user_name = argv #in this case user_name has to be given a name in the TERMINAL
prompt = "> " #prompt is initialized as a string (> )
#Let's try something else
# prompt = " estrin" #Everytime that an imput from the user is required,
# it writes whatever the string has been set as, that is why it was initially >
#to make it clear that an imput from the user is required

print(f"Hi {user_name}, I'm the {script} script")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice
""")
