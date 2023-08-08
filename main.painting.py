from turtle import Turtle, Screen
'''
# code to import the colors from the image and divide them in rgb
import colorgram as cg


# color_list = cg.extract('hirst.lamorteanonce.jpg', 30)
# color_palette = []
#
# for i in range(len(color_list)):
#     r = color_list[i].rgb.r
#     g = color_list[i].rgb.g
#     b = color_list[i].rgb.b
#     new_color = (r, g, b)
#     color_palette.append(new_color)
#
# print(color_palette)
# print(color_list)
'''

# the list was created from the code above
color_list = [(217, 166, 97), (251, 217, 154), (240, 199, 122), (152, 88, 39), (188, 146, 39), (69, 44, 16), (88, 77, 19), (219, 90, 59), (77, 104, 79), (153, 28, 9), (71, 88, 100), (36, 48, 60), (40, 55, 42), (124, 70, 76), (143, 162, 144), (47, 81, 38), (50, 36, 42), (216, 74, 79), (112, 142, 104), (133, 23, 29), (250, 175, 137), (125, 141, 148), (247, 200, 2), (50, 61, 81), (167, 138, 145), (47, 71, 76), (111, 134, 139), (183, 197, 173), (126, 126, 136)]

'''
Code to create a Hirst painting using the Turtle graphics module
'''

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.penup()
xpos = -300
ypos = -300
tim.setpos(xpos, ypos)

move_increase = 0
print(len(color_list))
for j in range(3):
    round_going = False
    while not round_going:
        for i in range(len(color_list)):
            l = 0
            j = 1
            k = 2
            red = color_list[i][l]
            green = color_list[i][j]
            blue = color_list[i][k]
            tim.dot(20,(red, green, blue))
            tim.penup()
            tim.forward(50)
            # tim.pendown()
            if i in (9, 19, 28):
                print(i)
                xpos = -350
                move_increase += 50
                tim.penup()
                tim.goto(xpos, ypos + move_increase)
                tim.forward(50)
                # tim.pendown()
            else:
                round_going = True





screen.exitonclick()
