# Even more practice
def break_words(stuff):
    """This funnction will break up word for us.""" #The words between the triple-double quotes is documentation comment, using the help() command it is possible to read such comment.
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Print the first word after popping it off."""
    word = words.pop(0) #The pop removes an element from a list. In this case it removes the first element (0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)#Removes the las element of a list (-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one,"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# In this one, we will run things differently
# We will import it into pyhton directly
#To do this we open the terminal and write py
# Now it is possible to write code on it as if it were a script.
# we can import a script by typing: import ex25
# But a much better way to do so is like this: from ex25 import *
# This basically lets us import every function that is in the ex25.py file, and makes it easier to call the function because it removes the need to write ex25.function every single time
