# --- DAY 16: STRINGS PT6 ---

# String find()
# Find where a character or word appears
sentence = "I love python programming"

index = sentence.find("Python")
print(index)   # Output: 7  (that's where "Python" starts)
# (if it can not find the word it returns -1)

# in keyword
# Check if something is inside a string
sentence = "I love Python programming"

print("Python" in sentence)   # True
print("Java" in sentence)   # False

# --- MINI CHALLENGE ---

phrase = " Day 16 of Python Challenge! "

# 1. Find where "Python" starts in the phrase
print(phrase.find("Python"))

# 2. Check if "challenge" is in the phrase (ignore case)
print("challenge" in phrase.lower())

# 3. Remove extra spaces
print(phrase.strip())

# --- REFLECTION ---

# Today I decided to to learn more string methods.
# I have also decided that I will be learning more about computers to support my computer science subject.
# When I say learning more about the computers, I mean like the hardware components, the different types of computers and so on.
# Today I have added more to my knowledge on strings. I realised yesterdays revision lesson really helped me !
# I will keep going!
