import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
player = input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors." )

computer = random.randint(0,2)
choice = [rock, paper, scissors]
print(choice[int(player)])
print(f"Computer chose: {computer} ")

print(choice[computer])

if int(player) >= 3 and int(player) < 0:
  print("You typed an invalid number, you lose! ")
elif int(player) == 0 and computer == 2:
  print("You win ") # Rock wins against scissors.
elif computer == 0 and int(player) == 2:
  print("You loose") 
elif int(player) == 2 and computer == 1:
  print("You win ") #Scissors win against paper.
elif computer == 2 and int(player) == 1:
  print("You loose")
elif int(player) == 1 and computer == 0:
  print("You win ") #Paper wins against rock.
elif computer == 1 and int(player) == 0:
  print("You loose")
else:
  print("It\'s a draw")


  