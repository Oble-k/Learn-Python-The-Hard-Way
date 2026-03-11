#Reading files
#There is another file named ex15_sample
# Our objective is to open that file without "Hard coding" our script
# Hard coding means putting some information that should come from the user as a string directly in our source code
# Reasoning being that we may work with other files later

#The next 2 lines, use argv to get a Filename
from sys import argv
script, filename = argv
#in the next line we have a new command open()
#The open function returns a file object that can be used to read, write and modify de file
txt=open(filename)

print(f"Here's your file {filename}: ")
# On the next line, we called a function (Read). We give a file a command by using the dot (.), the name of the command and te parameters.
print(txt.read()) #txt.read() is like asking txt to do the read command without a parameter

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

#No pude hacerlo funcionar en la uni, probar en casa
# En la uni no puedo modificar el PATH (enviroment variables) por no ser admin