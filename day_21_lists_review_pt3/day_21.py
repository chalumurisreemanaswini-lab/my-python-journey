# --- DAY 21: LISTS REVIEW + ONE NEW THING ---

# 1. Review a list I already know.
colours = ["red", "blue", "green"]
print(colours)
print(colours[1])
print(len(colours))

# 2. New list method: insert()
# (Add an item at a specific position
colours = ["red", "blue", "green"]

colours.insert(1, "yellow")
print(colours)   # ['red', 'yellow', 'blue', 'green']

# 3. Loops + condition: Print only colours that start with "b"
colours = ["red", "blue", "green", "black", "brown"]

for colour in colours:
  if colour.startswith("b"):
    print(colour)

# 4. Mini challenge!
fruits = ["apple", "banana", "cherry"]

# Add 'orange' at position 2
fruits.insert(2, "orange")

# Print all fruits
for fruit in fruits:
  print(fruit)

# --- REFLECTION ---

# I had to take a day off yesterday as I had gotten even more unwell than the day before yesterday.
# I was unable to code but i'm glad I am back now.
# I decided to take things easy by going over what I had learned already and one extra new thing.
# Today's set up is quite similar to day 20.
# I hope I will get better soon!
