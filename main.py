from turtle import Turtle, Screen
import pandas as pd


screen = Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
t = Turtle(shape=image)


# def get_mouse_click_coor(x, y):
#     print(x, y)
# screen.onscreenclick(get_mouse_click_coor)
# screen.mainloop()


data = pd.read_csv('50_states.csv')
states_list = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_state)}/50 Guess The State',
                                    prompt="What's another state'sname?").title()
    if answer_state == 'Exit':
        break

    if answer_state in states_list:
        t1 = Turtle()
        t1.hideturtle()
        t1.penup()
        state_data = data[data.state == answer_state]
        t1.goto(int(state_data.x), int(state_data.y))
        t1.write(state_data.state.item())
        guessed_state.append(answer_state)

for state in guessed_state:
        states_list.remove(state)

data = pd.DataFrame(states_list)
data.to_csv('new_miss.txt')


screen.exitonclick()