name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74*2.54 # inches
weight = 180*0.453592 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} centimeters tall.") # was inches
print(f"He's {weight} kilograms heavy.") # was pounds
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")