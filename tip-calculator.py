#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
bill = input("What was the total bill? ")
plain_bill = bill[1:]
tip_perc = input("What percentage bill would you like to give? 10, 12, or 15? ")
tip_perc = 1+round((int(tip_perc)/100), 2)

people = int(input("How many people to split the bill? "))

#pay = (float(plain_bill)/people)*tip_perc
pay = round((float(plain_bill)/people)*tip_perc, 2)
print("Each person should pay $"+str(pay))