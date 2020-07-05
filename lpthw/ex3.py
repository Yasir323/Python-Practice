my_name = "Zed A. Shaw"
my_age = 35
my_height = 74
my_weight = 180
my_eyes = "Blue"
my_teeth = "White"
my_hair = "Brown"

print("Let's talk about %s." %my_name)
print("He's %d inches tall." %my_height)
print("He's %d pounds heavy." %my_weight)
print("He's got %s eyes and %s hair."%(my_eyes, my_hair))
print("If i add %d, %d, and %d I get %d." %(my_age, my_height, my_weight, my_age+my_height+my_weight))


print(f"Let's talk about {my_name}")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
total = my_age + my_height + my_weight
print(f"If i add {my_age}, {my_height} and {my_weight}, I get {total}")
print(f"If i add {my_age}, {my_height} and {my_weight}, I get {my_age + my_height + my_weight}")
