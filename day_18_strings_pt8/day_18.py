# --- DAY 18: STRINGS + USER INPUT ---

# 1. Getting input from user
name = input("What is your name?")
print("Hello", name)
# Whatever you type becomes a string

# 2. Input + string formatting
name = input("What is your name? ")
age = input("How old are you? ")

print(f"Hi {name}, you are {age} years old.")

# 3. Checking input
favourite_language = input("What is your favourite language?")

if favourite_language.lower() == "python":
  print("Great choice!"
else:
  print("That's cool too!")

# 4. Small interactive string project
word = input("Enter a word: ")
print("Length:", len(word))
print("Uppercase:", word.upper())
print("Reversed:", word[::-1])

# --- RELFLECTIONS ---

# Today I used strings with user input.
# I am pretty sure this will be my last day on the topic of strings.
# Ofcourse I will continue it, just possibly more in the future if I were to revise or learn more advanced codes.
# For now, most of what is important for beginners like me learning the topic of strings has been covered.
# Get ready for a new topic tomorrow and a fresh start for the beginning of February!
