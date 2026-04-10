# Dictionaries, Oh Lovely Dictionaries
# A dictionary or dict is a way to store data, like a list but instead of using only numbers to get the data, you can use almost anything
# This means that dict works like a database for storing and organizing data
stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 +2}
print(stuff['name'])
print(stuff['age'])
print(stuff['height'])
stuff['city'] = "SF"
print(" ")

# print(stuff['city'])

for x in stuff:
    print(stuff[x])


# stuff[1] = "Wow"
# stuff[2] = "Neato"
# print(stuff[1])
# print(stuff[2])
print(" ")
print(stuff)
print("Now, let's delete something form the dictionary")

stuff.pop('city')
stuff.pop('height')
# stuff.pop(1)
# stuff.pop(2)

print(stuff)