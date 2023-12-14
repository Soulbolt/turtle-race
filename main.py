import random
from turtle import Turtle, Screen


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
# Assign colors, positions and create a set number of turtles(6) in a dynamic way instead of hard coding.
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
# Create a turtle list add each turtle created into list for easy access
turtle_list = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    # Loop to check each turtles position and make them move until they reach the goal, declare if user wins or loses
    for turtle in turtle_list:
        winning_color = turtle.pencolor()
        if turtle.xcor() < 230:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)
        else:
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle wins the race!")
            else:
                print(f"You've lost! The {winning_color} turtle wins the race!")
            is_race_on = False

screen.exitonclick()
