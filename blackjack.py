############### Blackjack Project #####################
import random
import replit
from art import logo
def main_game():
  replit.clear()
  print(logo)
#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  user_cards = []
  computer_cards = []
  def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
  #deal_card()
  #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
  #user_cards = []
  #computer_cards = []
    
  def calculate_score(user_cards, computer_cards):
    sum1 = sum(user_cards)
    sum2 = sum(computer_cards)
    if sum1 == 21:
      sum1 = 0
    elif sum2 == 21:
      sum2 = 0
    elif sum1 > 21:
      for j in range(len(user_cards)):
        if user_cards[j] == 11:
          i = 11
          user_cards.remove(i)
          user_cards.append(1)
          print(user_cards,"we converted 11 to 1 ")
          sum1 = sum(user_cards)
      
    return sum1 , sum2
    # print(sum1)
    # print(sum2)
  def compare(sum1, sum2):
    if sum1 > sum2:
      print("player looses")
    elif sum1 == sum2:
      print("it's a draw")
    elif sum2 > sum1:
      if sum2 <= 21:
        print("computer wins ")
      else:
        print("computer looses")  
      
  game_going = True
  print("game starts")
  
  
  for i in  range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
  print(f"begin draw for user: {user_cards}")
  print(f"begin draw for computer: {computer_cards}")
  print(f"computer's first card is: {computer_cards[0]}")
    
  while game_going:
    sum1, sum2 = calculate_score(user_cards, computer_cards)
    print(f"current sum user : {sum1}")
    print(f"current sum computer : {sum2}")
    if sum2 == 0:
      game_going = False
      print(" Computer got blackjack game over")
    elif sum1 == 0:
      game_going = False
      print("User got blackjack game over")
    elif sum1 > 21:
      game_going = False
      print("User got above 21 game over")
    # if sum1 == 0 or sum2 == 0 or sum1 > 21:
    #   game_going = False
    #   print("someone got blackjack")
    else:
      playing = input("do you want to continue playing y, n: ")
      if playing == "n":
        while sum2 < 17:
          computer_cards.append(deal_card())
          print(f"current cards for computer: {computer_cards}")
          sum1, sum2 = calculate_score(user_cards, computer_cards)
        game_going = False
        compare(sum1, sum2)   
      else:
        user_cards.append(deal_card())
        #computer_cards.append(deal_card())
        print(f"current cards for user: {user_cards}")
        #print(computer_cards)
  
  
        
  print(sum1)
  print(sum2)

  baby = input("Do you want to continue playing?: ")

  if baby == "y":
    main_game()
  else:
    print("game over, good bye....")

main_game()

  

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

