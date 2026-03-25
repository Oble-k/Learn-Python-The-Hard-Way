#More Files
from sys import argv
from os.path import exists
# Using import is a way to get free code from other, better programmers
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# ~~We could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()
# in_file, indata = open(from_file), in_file.read()

# print(f"The input file is {len(indata)} bytes long") # len is length, gives the length in bytes of a file

# print(f"Does the output file exist? {exists(to_file)}") #The command exists returns a True if the file exists
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()