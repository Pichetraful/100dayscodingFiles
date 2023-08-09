from turtle import Turtle, Screen


screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)


colors = ["purple", "green", "yellow", "orange", "red", "blue"]

'''
code to manually create the 5 turtles
further down you see another faster way to create the same'''
'''
xpos = -230
ypos = -100
purple = Turtle(shape="turtle")
purple.speed(1)
purple.color("purple")
purple.penup()
purple.goto(xpos, ypos)


green = Turtle(shape="turtle")
green.speed(1)
green.color("green")
green.penup()
green.goto(xpos, ypos+25)

yellow = Turtle(shape="turtle")
yellow.speed(1)
yellow.color("yellow")
yellow.penup()
yellow.goto(xpos, ypos+50)

orange = Turtle(shape="turtle")
orange.speed(1)
orange.color("orange")
orange.penup()
orange.goto(xpos, ypos+75)

red = Turtle(shape="turtle")
red.speed(1)
red.color("red")
red.penup()
red.goto(xpos, ypos+100)
'''

'''
second code to do the turtle race begin 
this has less code than the previous one'''

'''y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])'''

'''
third code to do the turtle race begin
'''
xpos = -230
ypos = -100

for i in colors:
    tim = Turtle(shape="turtle")
    tim.color(i)
    tim.penup()
    tim.goto(xpos, ypos)
    ypos +=30



screen.exitonclick()