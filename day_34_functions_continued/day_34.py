# --- DAY 34: FUNCTIONS CALLING OTHER FUNCTIONS ---

# 1. First function.
def greet(name):
  print("Hello", name)
  # This function just greets someone.

# 2. Second function
def welcome(name):
  greet(name)
  print("Welcome to Python!")

# Notice this line:
greet(name)

# That means call the greet function

# 3. Run the program
def greet(name):
  print("Hello", name)

def welcome(name):
  greet(name)
  print("Welcome to Python!")

welcome("Sam")

# Output:
# Hello Sam
# Welcome to Python

# EXERCISE: 

def square(n):
  return n * n

def show_square(n):
  result = squre(n)
  print("The square is", result)

show_square(5)

# --- REFLECTION ---

# Today I built on to the recap from yesterday.
# I think the muscle memory and understanding has made learning/ adding on knowledge a lot easier.
# I can definetly see improvement.
# I need to make sure to keep going in this pace and hopefully before I know it, I will have mastered the foundation of python.

