# --- DAY 31: FUNCTIONS ---

#  What is a function?
# A function is a block of code that does one thing.
# You can run it whenever you want without rewriting it.

# Example:
def greet():
  print("Hello, world!")

greet()
greet()

# Output:
# Hello, world!
# Hello, world!

# def greet (): - defines the function
# greet() - calls the function

# 2. Functions with parameters
# Functions can tale input to work with different values.
def greet(name):
  print("Hello", name, "!")

greet("Alice")
greet("Bob")

# Output:
# Hello Alice !
# Hello Bob !

# name is a parameter
# You can use it inside a function

# 3. Functions that return values
# Some functions give back a result.
def add(a, b):
  return a + b

result = add(5, 3)
print(result)

# Output:
# 8

# I have been taking down notes the entire time so now it is time for my own practical activity!

# 4. Mini exercise
# write a function called square that takes a number and returns it square.

# My code

def square(a):
  return a ** 2

result = square(8)
print(result)

# --- REFLECTION ---

# Today was a very writing based file.
# But it was definetly necessary, theory is also important.
# But to mix up things I added a practical aswell.
# The learning went pretty smooth today.
# I did make sure to search up any questions I had since it is better to understand, not memorise.



