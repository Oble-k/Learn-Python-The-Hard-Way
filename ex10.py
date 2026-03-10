#A scape sequence is a special combination of characters that star with a backslash \ and it makes up a character
#that can't be written directly or that has a special meaning in a string of text
print("I am 6'2\" tall.")
# print("I am 6'2" tall.")
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
# \t TABS the whole line
#if we write a string using the triple-double quotes
#and write multiple lines of code, each line will print in a different line
fat_cat="""
I'll do a list:
\t* Cat food
\t* Fishies \n
\t* Woolball
\t* Catnip\n\t* Cats"""
weird="""
\\
\'
\"
\awhat
\bhow
\ffor
\nnay
\rCarry
\ttabula"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(weird)