# --- DAY 30: FINAL NOTES ON WHILE LOOPS

# 1. What is a While Loop?
# A while loop repeats code while a condition is true
# Basic structure:
count = 0

while count < 5:
  print(count)
  count += 1

# Explanation:
# Start with count = 0
# Loop runs while count < 5
# count += 1 increases the number
# When count becomes 5, the loop stops

# Output:
# 0
# 1
# 2
# 3
# 4

# 2. Why we update variables
# If we don't change the variable, the loop might run forever.

  # Bad example:
  x = 1

while x < 5:
  print(x)
# This creates an infinite loop because x never changes/

# Correct version:
x = 1

while x < 5:
  print(x)
  x += 1

# 3. While Loops with user input.
# Loops can repeat until the user enters something specific

# Example:
password = ""

while password != "python":
  password = input("Enter the password")

print("Access granted")
# The program keeps asking until the correct password is entered

# 4. While loops with counting
# Whle Loops are often used for counting or repeating actions.

# Example:
number = 1

while number <= 5:
  print("Number:", number)
  number += 1

# Output:
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Number: 5

# 5. Using break to stop a loop
# break immediately stops the loop

# Example:
while True:
  name = input("Enter your name (type stop to quit: ")

if name == "stop":
  break

print("Hello", name)
# The loop continues until the user types "stop".

# 6. Infinite loops (Sometimes useful)
# An infinite loop runs forever unless something stops it.

# Example:
While True:
print("Are we home yet?")
# We usually combine this with break


# --- KEY THINGS TO REMEMBER ---
# WHILE LOOPS NEED 3 IMPORTANT PARTS:

# 1. A startimg variable
count = 0

# 2. A condition
while count < 5:

# 3. A change inside the loop
count += 1
# without the change, the loop might never stop.

# --- REFLECTION ---

# I now finally wrapped up this topic.
# I made this file into a like an all-in-one While Loops guide based on everything I had already learned.
# I am truly proud of my now 30 Day milestone of my python journey.
# All I know for a fact is that this journey will keep going! :)
