import turtle
from turtle import Turtle,Screen
import pandas

screen= turtle.Screen()
screen.title("U.S States Game")
image= "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("50_states.csv")
all_state=data.state.to_list()
guessed_states=[]

while len(guessed_states) <50:
    answer_state =screen.textinput(title=f"{len(guessed_states)}/50 State Correct",prompt="What's another state's name?").title()
    print(answer_state)
    if answer_state == "Exit":
        #Missing states to learn
        missing_states=[state for state in all_state if state not in guessed_states]
        # missing_states=[]
        # for  state in all_state:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_state:
        guessed_states.append(answer_state)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state == answer_state] #get the show where the answer matches
        t.goto(int(state_data.x),int(state_data.y))
        # t.write(state_data.state.item())
        t.write(answer_state)


#States to learn.csv




