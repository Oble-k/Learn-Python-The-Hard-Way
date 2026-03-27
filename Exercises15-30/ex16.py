# Reading and Writing files
from sys import argv

script, filename = argv #In the terminal we give the name of the file
print(f"We're going to erase {filename}.") #Such name is displayed on this print line
print("If you don't want that, hit CTRL-C (^C)") #Just a print line
print("If you do want that, hit RETURN.")#Another print

input("?")#An input that really doesn't matter what you put on it, as it can't save the info

print("Opening the file...")
# target = open(filename) #Let's try and remove the mode w from  the open.
# It seems that an error occurs in the truncate function. It can't write on the file, because by default it is in read mode only.
#And thus it is not possible to truncate, if the file is opened in the read mode
target = open(filename, 'w') #Open is in mode w, which stands for write
# print("Truncating the file. Goodbye!")
# target.truncate() #If the file is not on write mode there is an error: io.UnsupportedOperation: truncate
#There is also one question left. If the file test.txt is empty, maybe there is no reason to truncate it. But what if it is not empty?.

#I believe that, if you open a file in write mode, it truncates the file first. Thats what I found on the internet: https://docs.python.org/3/library/functions.html
#That is why it is not required to target.truncate() the file
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these on the file.\n")
lines=f"{line1}\n{line2}\n{line3}"
# Study drill 3
target.write(lines) #With this and the previous line we managed to write lines on the txt file using only a single target.write
# target.write(line1, "\n", line2, "\n", line3,"\n") #This one does NOT work

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

#Study drill 2, in the next 3 lines of code.
print("Now we will read the file:\n")

target = open(filename, 'r') #Remember, if we want to read a file, its important first to change it to mode r (Read)
print(target.read())

print("And finally, we close it.")
target.close()