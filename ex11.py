#input() is a prompt that lets the user introduce a variable
print("How old are you?", end=' ')
age = int(input())
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy")

print(f"Here is your age multiplied by seven {age*7}")