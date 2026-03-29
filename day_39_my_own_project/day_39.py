# --- DAY 39: MW OWN PROJECT ---

def welcome_player():
  player_name = input("What is your name")
  print("Welcome to the Mini Text Adventure game!")
  print("your name is", player_name)
  return player_name

def first_choice(name):
  print("You now have two options:")
  option_one = input("Choose: left or right?").lower()
  if option_one == "left":
    print("Wow! You have found a cat.")
  elif option_one == "right":
    print("Wow! You have found a dog.")
  else:
    print("Please choose either left or right")

def second_choice():
  print("Uh oh! The animal is going to attack you!")
  option_two = input("Choose: fight or run").lower
  if option_two == "fight":
    print("Oh no! The animal bit you")
  elif option_two == "run":
    print("You have escaped!")

player_name = welcome_player()
first_choice(player_name)
second_choice()

# --- REFLECTION ---

# I had so much fun creating a simple text game.
# I would really like to make another one like this but with more of an immersive story.
# Now I just really gave myself ideas.
# Day 39 was a great way to include many things I had learned and include functions.
# One thing I forgot to add before was the 'return player_name' on line 7.
# Without it, the name would have never returned.
  
    
    
