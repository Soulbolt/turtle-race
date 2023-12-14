from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
# Assign colors, positions and create a set number of turtles(6) in a dynamic way instead of hard coding.
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    don = Turtle(shape="turtle")
    don.color(colors[turtle_index])
    don.penup()
    don.goto(x=-230, y=y_positions[turtle_index])







screen.exitonclick()
