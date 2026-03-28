# While Loops
def while_loop(top,increment):
    i = 0
    numbers = []
    while i < top:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += increment
        print("Numbers now: ", numbers)
    return numbers

topnum = int(input("Enter a number: "))
incr = int(input("Enter the increment: "))

final_list = while_loop(topnum,incr)

print("The numbers: ")
for num in final_list:
    print(num)

# for num in numbers:
#     print(num)
