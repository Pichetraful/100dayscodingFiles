#import the libraries in needed files
from game_data import data
from art import logo, vs
from random import randint
import replit

#get the number of records in the dictionary
max_val = len(data)-1
#pick 2 random numbers
pick_number = randint(0, max_val)
pick_number2 = randint(0, max_val)
#if both numbers are the same, then pick again the second number
if pick_number2 == pick_number:
  pick_number2 = randint(0, max_val)
  
higher = ''
global counter
counter = 0

def compare(pick_number, pick_number2, higher, counter):
  '''check the score for the follower_count of each element in the dictionary
  if the the guess is wrong game is over'''
  
  if higher == "a":
    if data[pick_number]['follower_count'] > data[pick_number2]['follower_count']:
      #print(f"{data[pick_number]['name']} has more followers")
      counter += 1
      game_over = False
      return game_over, counter
    else:
      #print(f"{data[pick_number2]['name']} has more followers")
      #print("game over")
      game_over = True
      return game_over, counter
  else:
    if data[pick_number2]['follower_count'] > data[pick_number]['follower_count']:
      #print(f"{data[pick_number2]['name']} has more followers")
      counter += 1
      game_over = False
      return game_over, counter
    else:
      #print(f"{data[pick_number]['name']} has more followers")
      #print("game over")
      game_over = True
      return game_over, counter
      
def welcome(pick_number, pick_number2, counter, game_over):
  '''repeat the print of the logo's and get the value for A or B
  also check if game is over'''
  while not game_over:
    replit.clear()
    print(logo)
    if counter != 0:
      print(f"Your current score is: {counter}")
    print(f"Compare A: {data[pick_number]['name']}, a {data[pick_number]['description']}, from {data[pick_number]['country']}.")
    print(vs)
    print(f"Against B: {data[pick_number2]['name']},a {data[pick_number2]['description']}, from {data[pick_number2]['country']}.")
     
    higher = (input("Who has more followers? Type 'A' or 'B': ")).lower()
    game_over, counter = compare(pick_number, pick_number2, higher, counter)
    if game_over == True:
      replit.clear()
      print(logo)
      print(f"Sorry that's wrong. Final score: {counter}")
    pick_number = pick_number2
    pick_number2 = randint(0, max_val)
    if pick_number2 == pick_number:
      pick_number2 = randint(0, max_val)
welcome(pick_number, pick_number2, counter, game_over=False)
