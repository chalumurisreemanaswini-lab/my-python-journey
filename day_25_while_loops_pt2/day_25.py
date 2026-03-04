# --- DAY 25: WHILE LOOPS CONTINUED ---

# 1. Count Down Exercise
count = 5

while count > 0:
  print("Counting down", count)
  count -= 1   # subtract 1 each time

print("Blast off!")

# 2. Adding numbers until a total
total = 0
i = 1

while total < 20:
  total += i # add i to total
  print("Added", i, "-> total =", total)
  i += 1

# 3. User-controlled loop
number = 0

while number != 5:
  number = int(input("Enter a number (try 5): "))
  if number != 5:
    print("Nope, try again!")

# --- REFLECTION ---

# I decided to continue with while loops in multiple ways:
# counting down, summing numbers, and waiting for user input.
# I also will be a lot more busier from now on as we have the UKMT junior maths challenge.
# I for sure will revise for it all the days I possibly can.


