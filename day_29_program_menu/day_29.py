# --- DAY 29: MY MINI PROGRAM MENU ---

# The code:
while True:
  print("/n --- MINI PROGRAM MENU ---")
  print("1. Add two numbers")
  print("2. Subtract two numbers")
  print("3. Say hello")
  print("4. Exit")

  choice = input("Please choose an option 1-4: ")
  
  if choice == "1":
    a = float(input("Enter first number: "))
    b= float(input("Enter second number: "))
    print("Result:", a + b)
  elif choice == "2":
    a = float(input("Enter first number"))
    b = float(input("Enter second number"))
    print("Result:", a - b)
  elif choice == "3":
    name = input("What is your name?")
    print("Hello", name, "!")
  elif choice == "4":
    print("Goodbye!")
    break
  
  else:
    print("Invalid option, please try again")

# --- REFLECTION ---

# Today I made a mini program menu. I struggled a lot with the indentation.
# Luckily, after a while of trying to figure out the problem, I got through the obstacle myself.
# I am very proud of the code and I will wrap up on While loops tomorrow!
