# --- DAY 40: FINAL NOTES ON FUNCTIONS ---

# What is a function?
# A fucntion is a block of code that runs when you call it,
# It helps organise cide abd avoid repetition.

# Basic Function
def greet():
  print("Hello!")

grett()

# Functions with Parameters
def greet(name):
  print("Hello", name)

greet("Sam")

# - name is a parameter
# - You can pass different values each time

# Functions with return values
def add(a, b):
  return a + b

result = add(2,3)
print(result)

# - return sends a value back
# - You can store the result in a variable

# Defult Parameters

def greet(name="Friend"):
  print("Hello", name)

greet()
greet("Alex")

# - Uses a default value if no input is given

# Functions Calling Other Functions
def square(n):
  return n * n

def show_square(n):
  print("Square is", square(n))

show sqaure(5)

# - Functions can work together

# Functions with if/else
def check_event(n):
  if n % 2 == 0:
    print("Even")
  else:
    print("Odd")

# - You can use logic inside functions

# --- KEY POINTS ---
# - Use def to create a function
# - Use parameters to pass data
# - Usw return to send data back
# - Functons help make code reusable and organised

# --- REFLECTION ---

# Today I reviewed Python functions and everything I learned.
# My topic on functions has finally ended.
# Today marks the day I completed all the beginner python basic fundamentals.
# Last thing I need to do is try some challenges regarding the things I have learned.
# I can then move on to something a little harder.

