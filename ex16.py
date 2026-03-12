from sys import argv

script, filename = argv #In the terminal we give the name of the file
print(f"We're going to erase {filename}.") #Such name is displayed on this print line
print("If you don't want that, hit CTRL-C (^C)") #Just a print line
print("If you do want that, hit RETURN.")#Another print

input("?")#An input that really doesn't matter what you put on it, as it can't save the info

print("Opening the file...")
target = open(filename, 'w') #Open is in mode w, which stands for write

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these on the file.")
lines=f"{line1}\n{line2}\n{line3}"
target.write(lines) #With this and the previous line we managed to write lines on the txt file using only a single target.write
# target.write(line1, "\n", line2, "\n", line3,"\n") #This one does NOT work

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

#Study drill 2, in the next 3 lines of code.
print("Now we will read the file")

target = open(filename, 'r') #Remember, if we want to read a file, its important first to change it to mode r (Read)
print(target.read())

print("And finally, we close it.")
target.close()