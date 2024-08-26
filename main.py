import turtle, pandas
from show_turtles import Name_state

#data
Us_Map = "./blank_states_img.gif"
data = pandas.read_csv("./50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(Us_Map)
turtle.shape(Us_Map)
correct_states = 0
create_turtle = Name_state()
repeated = []


game_on = True
while game_on:
    list = data.state.to_list() 
    answer = screen.textinput(title=f"{correct_states}/50 States Correct", prompt="What's another state's name?").title()
    if answer == "Exit":
        game_on = False
        for item in repeated:
            list.remove(item)
        list_to_learn = pandas.DataFrame({"Left States":pandas.Series(list)})
        list_to_learn.to_csv("states_to_learn.csv")
    if answer in list:
        if answer in repeated:
            pass
        else:
            correct_states += 1
            name_states = data[data.state == answer]
            x = int(name_states.x)
            y = int(name_states.y)
            create_turtle.state_name(x,y,answer)
            repeated.append(answer)
    if correct_states == 50:
        game_on = False