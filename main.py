from turtle import Turtle, Screen
import random

#list for colous used for each turtle
colors = ["pink", "blue", "green", "black", "orange"]
#list for y cordiantes of each turtle
positions = [-190, -130, -90, -30, 0]


#functions

#bet function to display bet prompt
def bet():
    bet_color = screen.textinput("bet", "Enter the color of the turtle you want to bet on")
    return bet_color

#set function sets the positions  and colours of turtle and retruns a list
def set_turtles():
    turtles = []  # Create a list to store the turtle objects
    for i in range(5):
        new_turtle = Turtle("turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(-280, positions[i])
        turtles.append(new_turtle)  # Add the turtle to the list
    return turtles


#start race function starts the race and displays if we won or no
def start_race(turtles, bet_color):
    is_race_start = True
    while is_race_start:
        for turtle in turtles:
            random_num = random.randint(1, 10)
            turtle.forward(random_num)
            if turtle.xcor() >= 280:
                winner = turtle
                is_race_start = False
                stop()
                break  # Exit the loop if a turtle reaches the finish line
    if winner.color()[0] == bet_color:  # Checking the first element of the color tuple
        screen.textinput("You won", "Congratulations! You won the bet.")
    else:
        print("You lost the bet.")

#stop function stops the race and returns turtles to the center
def stop():
    for turtle in turtles:
            turtle.penup()  # Lift the turtle's pen to stop drawing
            turtle.setposition(0, 0)



screen = Screen()
screen.setup(width=600, height=600)
bet_color = bet()
set_turtles()
start_race(turtles, bet_color)
screen.exitonclick()
