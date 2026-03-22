# Functions and Files
from sys import argv

script, input_file = argv

def print_all(f): #Defines a function print_all
    print(f.read()) #Print on terminal every content of the f file

def rewind(f):
    f.seek(0) #Goes back to the index position #0 (Maybe byte 0?) (Yes it is dealing in bytes)
# What would happen if we didnt seek 0??
def print_a_line(line_count, f):
    print(line_count, f.readline(),end="") #What f.readline() does is read a line of a file until the \n, then stops. the next f.readline would read the following line.
#                                   ^ the end allows us to remove the extra \n character
# How does readline() know where each line is? Inside readline() is code that scans each byte of the file...
# ... until it finds a \n character, then stops reading the file to return what it found so far. The file...
# ... f is responsible for maintaining the current position in the file after each readline() call, so that
# it will keep reading each line

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file) #If we dont seek(0) the file has ended and thus, there will have nothing left to read
# This ^ means that we go back to the character #0, aka the first caracter

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file) #current_line = 1 ///Then, when the function is called we assign current_line to be line_count in the function that was defined

current_line += 1
print_a_line(current_line, current_file) #current_line = 2

current_line += 1
print_a_line(current_line, current_file) #current_line = 3