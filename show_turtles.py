from turtle import Turtle

class Name_state(Turtle):
    def __init__(self):
        super().__init__()

    def state_name(self,xpos, ypos, guessed_state):
        self.penup()
        self.hideturtle()
        self.goto(x=xpos,y=ypos)
        self.write(f"{guessed_state}", align="center", font=("Courier", 8, "normal"))