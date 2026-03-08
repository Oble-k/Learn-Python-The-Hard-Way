#This file is meant as a guide/learning method for list_functions
#This is the website I'm learning from == https://www.digitalocean.com/community/tutorials/how-to-use-list-methods-in-python-3
fish=['barracuda','cod','devil ray','eel'] #This creates a list. In this case with 4 string elements
# The list has 4 items, and their indexes range from 0 to 3. (0 is barracuda, 1 is cod and so on)

#We want to add yet another item to the list: we use list.append()
#note: "list" corresponds to the name that the list
fish.append('flounder') #This adds a new element to the END of the list.
print(fish) #Output(OP)==['barracuda', 'cod', 'devil ray', 'eel', 'flounder']

#But what if we wanted to add the item in a position other than the final one?
#Enter list.insert(i,x)
#i ---> numeric, index position in which you would like to add a new item.
#x ---> string (i.e. words), the item itself

fish.insert(0,'anchovy')  #This adds anchovy at the beginning of the list (index:0)
print(fish) #Output(OP)==['anchovy', 'barracuda', 'cod', 'devil ray', 'eel', 'flounder']
fish.insert(3,'damselfish')
print(fish) #Output(OP)==['anchovy', 'barracuda', 'cod', 'damselfish', 'devil ray', 'eel', 'flounder']

#What if we wanted 2 or more lists?
#Enter list.extend(L)
more_fish=['goby','herring','ide','kissing gourami'] #Just creating another list to merge it later
fish.extend(more_fish)  #This adds more_fish to the other list named fish. This changes list but not more_fish
print(fish)#Output(OP)==['anchovy', 'barracuda', 'cod', 'damselfish', 'devil ray', 'eel', 'flounder', 'goby', 'herring', 'ide', 'kissing gourami']

#Maybe we wanted to reduce the number of items in a list. How do we do it?
#Enter list.remove(x)
#This removes the first item on a list whose value is equal to x
fish.remove('kissing gourami')   #Removes kissing gourami from the list
fish.remove('damselfish') #Removes damselfish from the list
print(fish) #Output(OP)==['anchovy', 'barracuda', 'cod', 'devil ray', 'eel', 'flounder', 'goby', 'herring', 'ide']
#What if we try to remove an item that is not in the list?
# fish.remove('tuna fish')  ValueError: list.remove(x): x not in list --->There is an ValueError message

#Maybe we just want to check a particular item in the list. Then we use list.pop(i)
#i-->index
print(fish.pop(3)) #OP==devil ray
#Now our list should have one less item on it
print(fish) #OP==['anchovy', 'barracuda', 'cod', 'eel', 'flounder', 'goby', 'herring', 'ide']
#If we forgot to add a parameter, and we run fish.pop(), we would remove the last item from the list
#Sometimes lists get long. What if we wanted to determine at what index a certain value (item) is located?
#enter list.index(x)
#x--->item
print(fish) #OP==['anchovy', 'barracuda', 'cod', 'eel', 'flounder', 'goby', 'herring', 'ide']
print(fish.index('herring'))  #OP==6

#What if we wanted to manipulate a list, but also keep the original one unchanged?
#Enter list.copy()

# fish_copied = fish.copy() #This copies fish into fish_2// Doesn't work in versions earlier than 3.3
# print(fish_copied)
# print(fish)

#It is possible to reverse the order of the list using list.reverse()
fish.reverse()
print(fish) #OP==['ide', 'herring', 'goby', 'flounder', 'eel', 'cod', 'barracuda', 'anchovy']