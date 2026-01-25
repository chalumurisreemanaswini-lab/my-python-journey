# --- DAY 13: STRING SLICING (taking a piece) ---

# 1. Take the first letter.
language = "Python"
first_letter = language[0]
print(first_letter)   # RESULT: P

# 2. Take a chunk (A Slice)
# To get a chunk, you use a colon : inside the brackets [start : end].
# Note: Python stops before the last number.

# From seat 0 to seat 3 (gives us P, y, t)
chunk = language[0:3]
print(chunk) # RESULT: Pyt

# 3. Take the last letter
# A cool trick in Python is using -1 to get the very last letter without counting the whole word.
last_letter = language[-1]
print(last_letter)  # RESULT: n

# How could you use this in real life?
# Slicing is used in real life to pull out data out of codes.
# For example, if you have a data like 2026-01-25, you could just use a slice to grab out the 2026 part!

# --- RELFECTION ---

# Day 13, I learned to 'slice' strings today! It is sort of like using coordinates to find specific letters.
# I also learned that counting starts at 0 rather than 1.
# To take slices out of words is very useful if you just want certain parts of data.
# I am proud of what I have learned today! I will make sure to keep it up.
