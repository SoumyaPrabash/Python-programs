# import turtle
# import pandas
#
# screen = turtle.Screen()
# # screen.setup(width = 1000, height=600)
# screen.title("U.S. States Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
# screen.setup(width=800, height=600)
# turtle.shape(image)
# # answer_state = (screen.textinput(title="Guess the state", prompt="Whats another state's name?")).title()
# # print(type(answer_state))
# data = pandas.read_csv("50_states.csv")
# all_states_list = data.state.to_list()
# chances = True
# no_of_chances = 0
# correct = 0
# answers_list = []
# while chances:
#     answer_state = (screen.textinput(title=f"{correct} / 50 States Correct",
#                                      prompt="Whats another state's name?")).title()
#     no_of_chances += 1
#     if answer_state == "Exit":
#         break
#     if answer_state in all_states_list and no_of_chances < 50:
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         correct += 1
#         answers_list.append(answer_state)
#         state_detail = data[data.state == answer_state]
#         x_coordinate = int(state_detail.x)
#         y_coordinate = int(state_detail.y)
#         t.goto(x_coordinate, y_coordinate)
#         t.write(answer_state, align="center", font=("Arial", 8, "bold"))
#     elif no_of_chances == 50:
#         chances = True
#
# states_to_learn = [states for states in all_states_list  if states not in answers_list]
#
# df = pandas.DataFrame(states_to_learn)
# df.to_csv("to_learn")

from datetime import datetime

now=datetime.now()
DATE = now.strftime("%d/%m/%Y")
print(DATE)
TIME = now.strftime("%X")
print(TIME)
