# import colorgram
#
# rgb_colors=[]
#
# colors=colorgram.extract('img.jpg',30)
# for  color in colors:
#     r= color.rgb.r
#     g= color.rgb.g
#     b= color.rgb.b
#     new_color =(r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as turtle_module
import random


turtle_module.colormode(255)
tim =turtle_module.Turtle()
tim.penup()
tim.shape("turtle")
tim.hideturtle()
color_list=[(244, 242, 237), (228, 234, 241), (245, 237, 241), (235, 243, 238), (214, 157, 85), (33, 105, 151), (238, 215, 94), (153, 75, 52), (125, 168, 199), (209, 134, 163), (156, 60, 81), (22, 39, 54), (212, 85, 61), (176, 162, 47), (200, 85, 119), (135, 184, 150), (56, 119, 90), (240, 213, 4), (25, 46, 37), (228, 167, 186), (64, 46, 34), (87, 157, 100), (9, 99, 75), (34, 166, 189), (40, 60, 102), (228, 175, 166), (179, 189, 213), (95, 126, 173), (68, 34, 44), (105, 42, 60)]

tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots=100


for dot_count in range(1,num_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


