# --- DAY 28: GUESS THE NUMBER! ---

answer = int(input("Guess the number!"))
answer = answer.title()
counter = 1

while answer == "4":
  answer=input("Incorrect, try again! :)")
  answer = answer.title()
  counter = counter +1
print("Correct! You had", counter,"attempts.")

# --- REFLECTION ---

#  Today was a long day of volunteering so I decided to just whip up a code I learned recently.
# Volunteering was hectic but definetly worth the experience.
# I am just glad I pushed myself to post anyway eventhough it is quite late.
# I'll carry on with the consant posting dailt for sure!
