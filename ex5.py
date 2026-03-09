name = 'Zed A. Shaw'
age = 35
height_inch = 74.0 #inches
height_cm = round(height_inch * 2.54)
weight_lbs = 180 #lbs
weight_kg = round(weight_lbs/2.205)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_inch} inches tall.")
print(f"He's {weight_lbs} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffe.")

total = age + height_inch + weight_lbs
print(f"If i add {age},{height_inch} and {weight_lbs} I get {total}")

print(f"He's {height_cm} centimeters tall.")
print(f"He's {weight_kg} kilograms heavy. ")