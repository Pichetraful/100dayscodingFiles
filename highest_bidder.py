from replit import clear
from art import logo
print(logo)
def input_data():
  name = input("What is your name?: ")
  bid = input("What's your bid?: $")
  bid_tionary[name] = bid
#HINT: You can call clear() to clear the output in the console
print("Welcome to the secret auction program. ")
answer = "yes"
bid_tionary = {}
while answer:
  input_data()
  answer = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if answer == "no":
    answer = False
    clear()
  clear()
print(bid_tionary)
max_bid = max(bid_tionary.values())
max_bidder = max(bid_tionary, key=bid_tionary.get)
print(f"The winner is {max_bidder} with a bid of ${max_bid}")
    
    
    
