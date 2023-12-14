from turtle import Turtle, Screen

# Turtles characteristics
leo = Turtle()
leo.shape("turtle")
leo.penup()
mike = Turtle()
mike.shape("turtle")
mike.penup()
ralph = Turtle()
ralph.shape("turtle")
ralph.penup()
don = Turtle()
don.shape("turtle")
don.penup()
shane = Turtle()
shane.shape("turtle")
joan = Turtle()
joan.shape("turtle")
colors = ["red", " orange", "yellow", "green", "blue", "purple"]


# Assign each turtle a color based on the color list



screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")

leo.goto(x=-230, y=30)
leo.pendown()
mike.goto(x=-230, y=10)
mike.pendown()
ralph.goto(x=-230, y=-10)
ralph.pendown()
don.goto(x=-230, y=-30)
don.pendown()
screen.exitonclick()
