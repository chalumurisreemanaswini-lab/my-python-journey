# --- STRINGS - PATTERNS & COUNTING ---

# 1. Counting characters in a string
text = "banana"

print(text.count("a"))   # Output: 3
print(text.count("n"))   # Output: 2
# This matters because counting letters is used in data, games and text analysis.

# 2. Looping through a string 
word = "Python"

for letter in word:
  print(letter)
# This prints the letters one by one on different rows

# 3. Count vowels 
word = "programming"
vowels = "aeiou"
count = 0

for letter in word:
  if letter in vowels:
    count += 1

print(count)

#4. Reverse a string
word = "Python"
print(word[::-1])

# --- REFLECTION ---

# Today I practiced looping through strings and counting characters.
# I learned simple but effective codes like reversing strings or looping through a string.
# Today I learned multiple tricks and I will make sure to recall and to understand them before moving on.

# SIDE NOTE: I had computer science assessments that were coming up.
# It was also why I couldn't do my daily log as I was focused on other tasks in hand.
