#Number Guessing Game Objectives:
import random
from guess_art import logo
# Include an ASCII art logo.
print(logo)
def compare(counter):

  while counter > 0:
    print(f"You have {counter} attempts to guess the number")
    number = int(input("Make a guess: "))
    if number < num_to_guess:
      print("Too low")
      if counter > 1:
        print("Try again: ")
    elif number > num_to_guess:
      print("Too high")
      if counter > 1:
        print("Try again")
    elif number == num_to_guess:
      print(f"You got it, the answer was {num_to_guess}")
      counter = 0
    counter -= 1
    if counter == 0:
      print("You've run out of guesses, you lose")
      print(f"The number to be guesses was {num_to_guess}")
      
    
  
# Allow the player to submit a guess for a number between 1 and 100.
num_to_guess = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
diff_type = (input("Chose a difficulty, type 'easy' or 'hard' ")).lower()
if diff_type == "easy":
  counter = 10
  compare(counter)
elif diff_type == "hard":
  counter = 5
  compare(counter)
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 

# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

