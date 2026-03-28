# --- DAY 38: WHILE LOOPS RECAP ---
# It has been a while since I had done while loops. 
# Aswell as the breaks I have taken made it even longer.

# 1. Basic While loop
count = 1

while count <= 5:
  print(count)
  count += 1

# Prints number 1 to 5
# You control the loop with count

# 2. While Loop with User Input
name = ""

while name != "stop":
  name = input("Enter your name (type stop to quit): ")
  print("Hello", name)

# 3. While Loop with break 

while True:
  name = input("Enter your name (type stop to quit): ")

  if name == "stop":
    break

  print("Hello", name)

# MY CHALLENGE:

# Make a program that:
# Starts at 10
# Counts down to 1
# Prints "Done!" at the end

number = 10

while number >= 1:
  print(number)
  number -= 1

print("Done!)

# --- REFLECTION ---
# Today I got back into coding after a while of not being able to keep the streak.
# I will be more active on coding now for sure.
# I reviewed while loops and practiced coutning and using break.
# This helped me build my confidence and recalling what I already knew.










