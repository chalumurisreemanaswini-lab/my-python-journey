# --- DAY 24: WHILE LOOPS AND ARITHMETIC PRACTICE ---

# 1. What is a while loop?
# A while loop keeps running as long as the condition is true.
count = 0

while count < 5:
  print("Counting:", count)
  count += 1   # same as count = count + 1

# Output:
Counting: 0
Counting: 1
Counting: 2
Counting: 3
Counting: 4

# count += 1  is important, otherwise it could run forever

# 2. Simple arithmetic inside a loop
number = 1

while number <= 5:
  square = number * number
  print(f"{number} squared is {square}")
  number += 1

# Output:
1 squared is 1
2 squared is 4
3 squared is 9
4 squared is 16
5 squared is 25

# 3. "guess the number" game

secret = 7
guess = 0

while guess != secret:
  guess = int(input("Guess the number between 1 and 10"))
  if guess != secret:
    print("Try again!")

print("You guess the number! :)")

# --- REFLECTION ---

# I really enjoyed the mini challenge. We did it in school and I decided to see if I remembered the code.
# I chose While Loops for today's topic as I realised im not so confident with it.
# I also chose arithmetic to go with it as I am more confident with Artihmetic. 
# I thought if I combine it with a topic I am not so confident with, It may be easier for me to learn it.
# I will go through a video and some practice questions on While Loops to get more comfortable with it.

# I had to copy and paste this whole thing from a file I made that did not save :) I am glad I made sure to save it to clipboard just in case.
