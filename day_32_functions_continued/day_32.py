# --- DAY 32: FUNCTIONS CONTINUED ---

# 1. Function with two numbers.
def add(a, b):
  return a + b

result = add(3, 7)
print(result)

# EXPLANATION:
# a and b are parameters
# function returns the sum

#2. Function that prints instead of returning
# some functions do something instead of returning
def greet(name):
  print("Hello", name)

greet("Sam")

# DIFFERENCE:
# print() - shows something
# return() - sends a value back

# 3. Function with arithmetic
def multiply(x, y):
  return x * y

print(multiply(4, 5))

# OUTPUT:
# 20

# 4. Function + if statement
# Now we combine functions + conditionals
def check_even(number):
  if number % 2 == 0:
    print("Even number")
  else:
    print("Odd number")

check_even(6)
check_even(7)

# OUTPUT:
# Even number
# Odd number

# Mini Exercise
# Write a function called double that returns twice the number.

def double(n):
  return n * 2

print(double(5))

# --- REFLECTION ---

# Today I decided to build onto what I learned yesterday.
# I struggled to understand what def meant.
# In the end, I learned through some researching and now I am feeling a lot more confident to face functions.
# Tomorrow I will recall what I learned today and some other theory + code.




